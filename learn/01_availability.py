"""
LESSON 01 — Coverage and availability, from scratch.

This is the actual logic behind the Plant 175 proposal, written small enough
to read in one sitting. Run it with:   python 01_availability.py

Read it top to bottom. Every block has a WHY (the business rule) and a HOW
(the Python doing it). If you only understand the WHY on the first pass,
that is a completely fine first pass.
"""

# ---------------------------------------------------------------------------
# STEP 0 — Some fake plant data to work with.
# ---------------------------------------------------------------------------
# A "list" in Python is an ordered collection, written in square brackets.
# Each item here is a "dictionary" (curly braces): a set of name -> value pairs.
# This mimics what one hour of SCADA readings might look like for a few units.
#
# state meanings, straight from the report's state legend:
#   "up"      -> unit was measured and running
#   "down"    -> unit was measured and NOT running (real unavailability)
#   "silent"  -> the channel returned nothing at all (NOT the same as down!)

readings = [
    {"unit": "ESS-01", "hour": 0, "state": "up"},
    {"unit": "ESS-01", "hour": 1, "state": "up"},
    {"unit": "ESS-01", "hour": 2, "state": "down"},
    {"unit": "ESS-01", "hour": 3, "state": "up"},

    {"unit": "ESS-02", "hour": 0, "state": "up"},
    {"unit": "ESS-02", "hour": 1, "state": "silent"},
    {"unit": "ESS-02", "hour": 2, "state": "silent"},
    {"unit": "ESS-02", "hour": 3, "state": "silent"},
]

# The contractual threshold: below this much coverage, we do not publish
# a number. This is the single most important line in the whole file.
COVERAGE_THRESHOLD = 0.90   # 90%


# ---------------------------------------------------------------------------
# STEP 1 — Group the readings by unit.
# ---------------------------------------------------------------------------
# WHY: availability is calculated per unit, so we need each unit's readings
#      collected together before we can do anything.
# HOW: build an empty dictionary, then walk through every reading once and
#      file it under its own unit name.

by_unit = {}                          # start with an empty dictionary

for r in readings:                    # "for each reading r in the list..."
    unit = r["unit"]                  # look up the "unit" value in that dict

    if unit not in by_unit:           # first time we have seen this unit?
        by_unit[unit] = []            # then create an empty list for it

    by_unit[unit].append(r)           # add this reading to that unit's list

# After this loop, by_unit looks like:
#   {"ESS-01": [4 readings], "ESS-02": [4 readings]}


# ---------------------------------------------------------------------------
# STEP 2 — For each unit, calculate coverage and availability.
# ---------------------------------------------------------------------------
# This is where the real rule lives. Read the three counters carefully:
# they are the entire argument of Section 5 of your proposal.

def analyse(unit_readings):
    """Take one unit's readings, return its coverage and availability.

    A "function" is a named, reusable block. You call it with some input
    (unit_readings) and it hands something back (the return value).
    """

    total = len(unit_readings)        # len() = how many items in the list

    # Count how many readings were actually observed.
    # This is a "generator expression": for every reading, produce True or
    # False, then sum() adds up the Trues (Python counts True as 1).
    observed = sum(1 for r in unit_readings if r["state"] != "silent")

    # Of the observed ones, how many were actually running?
    up = sum(1 for r in unit_readings if r["state"] == "up")

    # Coverage = what fraction of expected readings we actually saw.
    coverage = observed / total

    # THE CRITICAL LINE.
    # Availability divides by `observed`, NOT by `total`.
    #
    # If we divided by total, every silent hour would be counted as downtime
    # and the number would be catastrophically, falsely low. That is exactly
    # the 54.41% error caught before it reached a PDF.
    #
    # Dividing by `observed` means: "of the time we could actually see,
    # this is how much it was up." Silence is excluded, not assumed.
    if observed == 0:
        availability = None           # None = "no value", not zero
    else:
        availability = up / observed

    return coverage, availability     # hand back both numbers


# ---------------------------------------------------------------------------
# STEP 3 — Report, and refuse to report when we can't substantiate.
# ---------------------------------------------------------------------------

print(f"{'UNIT':<10}{'COVERAGE':>10}{'AVAILABILITY':>15}   VERDICT")
print("-" * 55)

for unit, unit_readings in by_unit.items():     # .items() gives key AND value
    coverage, availability = analyse(unit_readings)

    # This is the gate. It "fails closed": the default is to withhold,
    # and a figure has to earn its way past the threshold to be published.
    if coverage < COVERAGE_THRESHOLD:
        verdict = "WITHHELD — coverage below threshold"
        shown = "—"                   # publish nothing, not a guess
    else:
        verdict = "Approved"
        shown = f"{availability:.1%}" # .1% formats 0.75 as "75.0%"

    print(f"{unit:<10}{coverage:>9.1%}{shown:>15}   {verdict}")

print()
print("Note ESS-02: it was 'up' every single hour it reported.")
print("A naive script would publish 100% availability and look correct.")
print("It was silent for 3 of 4 hours, so we have no basis for any claim.")
print("Saying nothing is the honest answer. That is the whole product.")
