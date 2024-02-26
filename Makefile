NAME=pywal
PREFIX=~/.local
CONF_PREFIX=$(HOME)/.config
WAL_TEMPLATES_DIR=/wal/templates

install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -vf scripts/apply-theme.sh $(DESTDIR)$(PREFIX)/bin/
	mkdir -p $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)
	cp -vf templates/pywal.svg $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)/$(NAME).svg
	cp -vf templates/pywal.json $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)/$(NAME).json
	cp -vf templates/pywal.kvconfig $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)/$(NAME).kvconfig

uninstall:
	rm $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)/$(NAME).svg
	rm $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)/$(NAME).json
	rm $(DESTDIR)/$(CONF_PREFIX)/$(WAL_TEMPLATES_DIR)/$(NAME).kvconfig
	rm $(DESTDIR)$(PREFIX)/bin/apply-theme.sh


.PHONY: install uninstall
