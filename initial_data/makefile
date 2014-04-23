PYTHON = python
GENERATE_SCRIPT = gen.py
TARGET = pieces.sql
TEMPLATE = tables.template
FOMMATER = 'NF>1 {printf("%s_rows.sql ", $$1)}'

initial_data:
	$(PYTHON) $(GENERATE_SCRIPT)
	cat `awk $(FOMMATER) $(TEMPLATE)` >> $(TARGET)
clean:
	rm -f *.sql
	



