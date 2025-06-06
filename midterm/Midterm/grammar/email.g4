grammar email;

start: EMAIL EOF;

EMAIL: LOCAL_SUBPART ('.' LOCAL_SUBPART)* '@' DOMAIN_SUBPART ('.' DOMAIN_SUBPART)+;

fragment LOCAL_SUBPART : [a-zA-Z0-9!$&()*+,;=:_~-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9-]+;
