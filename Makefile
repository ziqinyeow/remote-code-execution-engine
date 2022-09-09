cc:
	rm -rf **/*/__pycache__/

r:
	docker run --rm -d -p 6379:6379 redis