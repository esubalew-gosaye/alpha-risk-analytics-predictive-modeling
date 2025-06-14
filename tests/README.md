# Tests

This folder contains unit tests for data cleaning and preprocessing functions.

## test_date_cleaning.py

Tests the `clean_vehicle_intro_date()` function from `src/utils/clean_data.py`. Validates:

- Date format conversions:
  - Month/year formats (`6/2002`, `06/2002`)
  - Full date formats (`2020-06-15`, `15/06/2020`)
  - Datetime strings with time components
- Edge case handling:
  - Invalid dates (`13/2020`, `invalid`)
  - Empty/whitespace inputs
  - Null/NA values
- Timezone-naive date normalization

## Running Tests

### Basic test run:
```bash
pytest -v