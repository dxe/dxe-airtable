.PHONY: sync test-sync

sync:
	python2 airtable_to_mailing_list.py

test-sync:
	python2 test_airtable_to_mailing_list.py
