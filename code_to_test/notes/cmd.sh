# DYNAMOSA
## peak memory usage
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name matrix_calculus --assertion-generation NONE -v \
    --seed 1 \
    --algorithm DYNAMOSA \
    --maximum-search-time 300 \
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name matrix_calculus --assertion-generation NONE -v \
    --seed 1 \
    --constraints PEAK_MEMORY_USAGE \
    --algorithm DYNAMOSA \
    --test-case-memory-usage-limit 7500 \
    --maximum-search-time 300 \

## execution time
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name banking --assertion-generation NONE -v \
    --seed 1 \
    --algorithm DYNAMOSA \
    --maximum-search-time 300 \
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name banking --assertion-generation NONE -v \
    --seed 1 \
    --constraints EXECUTION_TIME \
    --algorithm DYNAMOSA \
    --test-case-execution-time-limit 100_000_000 \
    --maximum-search-time 300 \

# MOSA

# MIO

# RANDOM

# WHOLE_SUITE
## peak memory usage
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name matrix_calculus --assertion-generation NONE -v \
    --seed 1 \
    --algorithm WHOLE_SUITE \
    --maximum-search-time 300
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name matrix_calculus --assertion-generation NONE -v \
    --seed 1 \
    --constraints PEAK_MEMORY_USAGE \
    --algorithm WHOLE_SUITE \
    --test-suite-memory-usage-limit 9000 \
    --maximum-search-time 300

## execution time
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name banking --assertion-generation NONE -v \
    --seed 1 \
    --algorithm WHOLE_SUITE \
    --maximum-search-time 300
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name banking --assertion-generation NONE -v \
    --seed 1 \
    --constraints EXECUTION_TIME \
    --algorithm WHOLE_SUITE \
    --test-suite-execution-time-limit 600_000_000 \
    --maximum-search-time 300

# RANDOM_TEST_CASE_SEARCH

# RANDOM_TEST_SUITE_SEARCH
