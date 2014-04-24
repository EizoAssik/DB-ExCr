PYTHON = python
GENERATE_SCRIPT = gen.py
TARGET = pieces.sql
TEMPLATE = tables.seq
FOMMATER = '{printf("%s.sql ", $$1)}'

initial_data:
	$(PYTHON) $(GENERATE_SCRIPT) $(TEMPLATE)
	cat `awk $(FOMMATER) $(TEMPLATE)` >> $(TARGET)
clean:
	rm -f *.sql
	



