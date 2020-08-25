# Route53 and DNS Reverse

**Contents**
- [x] [DNS](#dns)
- [x] [Types of Record](#types-of-records)
- [x] [A record](#a-record)
- [x] [CNAMEs](#cname)
- [x] [Alias](#alias)
- [x] [MX Records](#mx-records)
- [x] [TTLs](#ttls)
- [x] [Propagation](#propagation)
- [x] [AWS Route 53](#)

## DNS

## Types of Records
```bash
A - Address Mapping

```

# A Record

## Alias 
Multiple ALIAS-records for same name / same type
You can have multiple ALIAS-records for the same name and record type - resolving records from multiple names and combining the results into one synthesized record set.
And yes, this works very well with the round robin option for load balancing.

Multiple ALIAS-records for same name / different types
You can have multiple ALIAS-records for the same name but different record types.
For example: yourname.com / A-records -> "webserv1.cloudoperator.com", and yourname.com / MX-records -> "smtp.othercompany.com".


This creates speed benefit. If an alias is defined as A record instead of standard CNAME, then managed service can resolve the secondary query and return an IP address

a CNAME record must always lead to an A record or a domain name. A CNAME record cannot lead to another CNAME record. You should also avoid setting other records in the DNS Zone to CNAME records. 

1. Make it possible to alias the root domain to another service
2. Make it possible to use an alias system that can coexist with other records

# CNAME
https://ns1.com/resources/cname

canonical name record 
canonical meaning - accurate, according to something that is recognisable

Search Results
Featured snippet from the web
CNAME records are typically used to map a subdomain such as www or mail to the domain hosting that subdomain's content.
 
For example, a CNAME record can map the web address www.example.com to the actual web site for the domain example.com.


Using this DNS configuration, when a visitor enters www.ralphsdomainname.com in their browser, they will get the answer of anotherdomain.com. The browser then needs to do an additional DNS look up to get the IP address of anotherdomain.com by asking for the A record.


The major advantage of using CNAME is that if we change the IP address of one A record then any CNAME record pointing to that host will also changed.



Difference between ALIAS and CNAME

The ALIAS Record, like CNAME, also maps a hostname to another hostname. However, the ALIAS Record makes it possible to have other DNS records on the same hostname, while CNAME does not. This makes it possible to apply ALIAS at the root domain (DNS zone apex), which is not allowed for CNAME.

In addition, ALIAS has better performance than CNAME because it does not require the DNS client to resolve another hostname - it directly returns an IP. However ALIAS records too need to do recursive lookups behind the scenes which can affect performance.

## MX Records

## TTLs
## Propagation

## Route 53