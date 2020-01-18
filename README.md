# usps_address_validation
 This uses the USPS API to validate addresess. This was thrown together when I was assigned to create address-labels for our wedding invitations. The provided addresess were in an inconsistant format, and some of the zip codes were incomplete. 
 

## Requirements

Python3.8 has been tested. This also requires the [pyusps](https://pypi.org/project/pyusps/) package to be installed 

```bash
pip3 install pyusps
```

## Usage

addresess.txt contains a tab-delimited list of addressees.

>City	State	Address	Zip Code
>
>Washington	DC	1600 Pennsylvania Ave NW	20501

Run AddressValidation.py, and the output will be written to output.txt.

>City	State	Address	Zip Code
>
>1600 PENNSYLVANIA AVE NW	WASHINGTON	DC	20500-0003

The tab-delimited files can be copied directly to/from excel.