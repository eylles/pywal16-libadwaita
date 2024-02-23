NAME=pywal
PREFIX=$(HOME)
LOCATION=/.config
WAL_TEMPLATES_DIR=/wal/templates

install:
	mkdir -p $(DESTDIR)/$(PREFIX)/$(LOCATION)/$(WAL_TEMPLATES_DIR)
	cp templates/pywal.svg $(DESTDIR)/$(PREFIX)/$(LOCATION)/$(WAL_TEMPLATES_DIR)/$(NAME).svg
	cp templates/pywal.json $(DESTDIR)/$(PREFIX)/$(LOCATION)/$(WAL_TEMPLATES_DIR)/$(NAME).json
	cp templates/pywal.kvconfig $(DESTDIR)/$(PREFIX)/$(LOCATION)/$(WAL_TEMPLATES_DIR)/$(NAME).kvconfig

uninstall:
	rm $(DESTDIR)/$(PREFIX)/$(LOCATION)/wal/templates/$(NAME).svg
	rm $(DESTDIR)/$(PREFIX)/$(LOCATION)/wal/templates/$(NAME).json
	rm $(DESTDIR)/$(PREFIX)/$(LOCATION)/wal/templates/$(NAME).kvconfig


.PHONY: install uninstall
