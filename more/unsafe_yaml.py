import yaml

# VULNERABLE: yaml.load() on untrusted input can lead to arbitrary code execution
data = request.GET.get("data")
conf = yaml.load(data)  # Allows instantiation of arbitrary Python objects

# SOURCE: https://www.bugs.gentoo.org/659348
