# memory usage
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name matrix_calculus --assertion-generation NONE -v \
    --seed 1 \
    --algorithm DYNAMOSA \
    --maximum-search-time 30
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name matrix_calculus --assertion-generation NONE -v \
    --seed 1 \
    --constraints MEMORY_USAGE \
    --algorithm DYNAMOSA \
    --test-case-memory-usage-limit 26000 \
    --maximum-search-time 30

# execution time
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name banking --assertion-generation NONE -v \
    --seed 1 \
    --algorithm DYNAMOSA \
    --maximum-search-time 30
python3 src/pynguin/__main__.py --project-path code_to_test/modules --output-path code_to_test/output --module-name banking --assertion-generation NONE -v \
    --seed 1 \
    --constraints EXECUTION_TIME \
    --algorithm DYNAMOSA \
    --test-case-execution-time-limit 100_000_000 \
    --maximum-search-time 30
