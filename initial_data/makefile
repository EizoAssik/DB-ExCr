HOME = ..

include $(HOME)/make.def

TARGET = pieces.sql
TEMPLATE = tables.seq
FOMMATER = '{printf("%s.sql ", $$1)}'

initial_data:
	$(PYTHON) $(GENSCRIPT) $(TEMPLATE)
	cat `awk $(FOMMATER) $(TEMPLATE)` >> $(TARGET)
clean:
	$(CLEANSQL)
	



