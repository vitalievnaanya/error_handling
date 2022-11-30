from errors import NameTooShortError, MustContainSymbolError, InvalidDomainError

valid_domains = {'com', 'bg', 'net', 'org'}

while True:
    email = input()
    if email == 'End':
        break

    email_parts = email.split('@')
    if len(email_parts) == 1:
        raise MustContainSymbolError('Email must contain @')
    if len(email_parts) > 2:
        raise  MustContainSymbolError('Email must contain only one @ sign')

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    domain_parts = domain_name.split('.')

    if len(domain_parts) < 2:
        raise InvalidDomainError('Invalid domain name')
    domain = domain_parts[-1]

    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
