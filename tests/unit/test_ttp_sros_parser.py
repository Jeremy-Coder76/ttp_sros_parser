"""Test SROS Parser."""
from ttp_sros_parser import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_templates_as_list(sros_parser):
    """
    Test to ensure all templates are imported as a list.
    """
    assert isinstance(sros_parser._get_all_templates(), list)


def test_get_router_interfaces(sros_parser, parsed_interfaces):
    """
    Test to ensure interfaces are extracted from the base context.
    """
    result = sros_parser.get_router_interfaces()
    assert result == parsed_interfaces


def test_get_system_interfaces(sros_parser, parsed_system_interface):
    """
    Test to retrieve the system interface only.
    """
    result = sros_parser.get_system_interface()
    assert result == parsed_system_interface


def test_get_system_configuration(sros_parser, parsed_system_configuration):
    """
    Test to retrieve the system configuration.
    """
    result = sros_parser.get_system_configuration()
    assert result == parsed_system_configuration


# def test_get_full_config(sros_parser, full_parsed_config):
#     """A full config str should be returned."""
#     result = sros_parser.get_full_config()
# TODO: "Update fixture contents + templates test this."


def test_get_system_hostname(sros_parser):
    """Test extracting hostname only."""
    result = sros_parser.get_system_hostname()
    assert result == "EXAMPLEPHX-P-AL-7750-01"


def test_get_system_cards(sros_parser, parsed_system_cards):
    """Test parsing system cards."""
    result = sros_parser.get_system_cards()
    assert result == parsed_system_cards


def test_get_system_maf(sros_parser, parsed_system_maf):
    """Test extracting system MAF IPV4/6 Filters."""
    result = sros_parser.get_system_maf()
    assert result == parsed_system_maf


def test_get_system_ethcfm(sros_parser, parsed_ethcfm):
    """
    Test extracting eth-cfm information
    """
    result = sros_parser.get_system_ethcfm()
    assert result == parsed_ethcfm


def test_get_system_asn(sros_parser):
    """
    Test extracting system asn
    """
    result = sros_parser.get_system_asn()
    assert result == "64500"


def test_get_custom_template(sros_parser):
    """
    Test running custom template.
    """
    template = "ttp_sros_parser/templates/custom/sros_custom_hostname_asn.ttp"
    result = sros_parser.get_custom_template(template_path=template)
    custom = [{"asn": {"router": {"autonomous-system": "64500"}}, "system": {"hostname": "EXAMPLEPHX-P-AL-7750-01"}}]
    assert result == custom


def test_get_system_service_sdp(sros_parser, parsed_system_sdp):
    """
    Test extracting system SDPs
    """
    result = sros_parser.get_system_service_sdp()
    assert result, parsed_system_sdp


# def test_get_router_static_routes():
#     """
#     Test extracting router static routes (BASE)
#     """
#     parser = SrosParser(example_config)
#     result = parser.get_router_static_routes()
#     routes = """[
# {
#     "router": {
#         "static-route": {
#             "ipv4": [
#                 {
#                     "default-route": [
#                         {
#                             "default-route": {
#                                 "bfd-enable": true,
#                                 "next-hop": "192.168.0.1"
#                             }
#                         },
#                         {
#                             "default-route": {
#                                 "next-hop": "192.168.10.1",
#                                 "preference": "10"
#                             }
#                         }
#                     ],
#                     "entry": [
#                         {
#                             "bfd-enable": true,
#                             "next-hop": "172.25.69.88",
#                             "prefix": "10.115.69.65",
#                             "prefix-length": "32"
#                         },
#                         {
#                             "next-hop": "172.25.69.88",
#                             "preference": "10",
#                             "prefix": "10.115.69.65",
#                             "prefix-length": "32"
#                         }
#                     ]
#                 },
#                 {
#                     "black-hole": {
#                         "black-hole": "black-hole",
#                         "prefix": "10.115.69.101/32"
#                     }
#                 }
#             ],
#             "ipv6": [
#                 {
#                     "default-route": [
#                         {
#                             "default-route": "::/0 next-hop 1001:1000:206a:31cd:645:400::/64 bfd-enable"
#                         },
#                         {
#                             "default-route": "::/0 next-hop 1001:1000:206a:31cc:645:400::/64 preference 10"
#                         }
#                     ],
#                     "entry": [
#                         {
#                             "bfd-enable": true,
#                             "next-hop": "1001:1000:206a:31cd:645:400::",
#                             "prefix": "1001:1000:2000:0:645:2a0::",
#                             "prefix-length": "128"
#                         },
#                         {
#                             "next-hop": "1001:1000:206a:31cd:645:400::",
#                             "preference": "10",
#                             "prefix": "1001:1000:2000:0:645:2a0:0:1",
#                             "prefix-length": "128"
#                         }
#                     ]
#                 },
#                 {
#                     "black-hole": [
#                         {
#                             "black-hole": "black-hole",
#                             "prefix": "1001:1000:2062:30cf::/64"
#                         },
#                         {
#                             "black-hole": "black-hole",
#                             "prefix": "1001:1000:2062:3634::/64"
#                         }
#                     ]
#                 }
#             ]
#         }
#     }
# }
# ]"""
#     assert result, routes


# def test_show_router_interface():
#     """
#     Test extracting router interfaces from show command
#     """
#     data = "tests/show_output/show_router_interface.txt"

#     parser = SrosParser(data)
#     result = parser.show_router_interface()
#     interfaces = """[
# {
#     "router": [
#         {
#             "interfaces": {
#                 "L3-TELCO-IXR01-1": {
#                     "address": [
#                         {
#                             "pfx-state": "INACCESSIBLE",
#                             "prefix": "2001:1000:2062:357a:646:100:0:1",
#                             "prefix-length": "64"
#                         },
#                         {
#                             "pfx-state": "INACCESSIBLE",
#                             "prefix": "2001:1666:2062:357a:646:100:0:1",
#                             "prefix-length": "64"
#                         },
#                         {
#                             "pfx-state": "INACCESSIBLE",
#                             "prefix": "fe80::645:100:0:1",
#                             "prefix-length": "64"
#                         }
#                     ],
#                     "admin-state": "Up",
#                     "ipv4": "Down",
#                     "ipv6": "Down",
#                     "mode": "IES",
#                     "port-sap-id": "lag-1:300"
#                 },
#                 "L3-TELCO-IXR02-1": {
#                     "address": [
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "2001:1666:2062:4222:649:100:0:1",
#                             "prefix-length": "64"
#                         },
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "fe80::645:100:0:1",
#                             "prefix-length": "64"
#                         }
#                     ],
#                     "admin-state": "Up",
#                     "ipv4": "Down",
#                     "ipv6": "Up",
#                     "mode": "IES",
#                     "port-sap-id": "lag-2:300"
#                 },
#                 "L3-TELCO-eNodeB0420-DUL-01": {
#                     "address": [
#                         {
#                             "pfx-state": "n/a",
#                             "prefix": "10.0.0.0",
#                             "prefix-length": "31"
#                         },
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "2001:1000:2062:24ae:649:100::",
#                             "prefix-length": "64"
#                         },
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "fe80::c8:ffff:fe00:0",
#                             "prefix-length": "64"
#                         }
#                     ],
#                     "admin-state": "Up",
#                     "ipv4": "Up",
#                     "ipv6": "Up",
#                     "mode": "IES",
#                     "port-sap-id": "1/1/c2/1:301"
#                 },
#                 "system": {
#                     "address": [
#                         {
#                             "pfx-state": "n/a",
#                             "prefix": "10.100.43.69",
#                             "prefix-length": "32"
#                         },
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "2001:4777:2062:2000:645:100:0:19f",
#                             "prefix-length": "128"
#                         }
#                     ],
#                     "admin-state": "Up",
#                     "ipv4": "Up",
#                     "ipv6": "Up",
#                     "mode": "Network",
#                     "port-sap-id": "system"
#                 },
#                 "to-7750-01": {
#                     "address": [
#                         {
#                             "pfx-state": "n/a",
#                             "prefix": "172.20.200.69",
#                             "prefix-length": "31"
#                         },
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "2001:1666:206a:335d:645:100:0:1",
#                             "prefix-length": "64"
#                         },
#                         {
#                             "pfx-state": "PREFERRED",
#                             "prefix": "fe80::c8:ffff:fe00:0",
#                             "prefix-length": "64"
#                         }
#                     ],
#                     "admin-state": "Up",
#                     "ipv4": "Up",
#                     "ipv6": "Up",
#                     "mode": "Network",
#                     "port-sap-id": "1/1/c4/1:3415"
#                 },
#                 "to-BTS0420-7750-H2": {
#                     "address": [
#                         {
#                             "pfx-state": "n/a",
#                             "prefix": "172.20.200.1",
#                             "prefix-length": "31"
#                         },
#                         {
#                             "pfx-state": "INACCESSIBLE",
#                             "prefix": "2001:1666:206a:335f:645:100::",
#                             "prefix-length": "64"
#                         },
#                         {
#                             "pfx-state": "INACCESSIBLE",
#                             "prefix": "fe80::c8:ffff:fe00:14b",
#                             "prefix-length": "64"
#                         }
#                     ],
#                     "admin-state": "Up",
#                     "ipv4": "Down",
#                     "ipv6": "Down",
#                     "mode": "Network",
#                     "port-sap-id": "lag-11:4094"
#                 }
#             }
#         },
#         {
#             "count": {
#                 "total": "6"
#             }
#         }
#     ]
# }
# ]"""
#     assert result, interfaces


# def test_get_system_profiles():
#     """
#     Test extracting system profiles
#     """

#     parser = SrosParser(example_config)
#     result = parser.get_system_profiles()
#     profiles = """[
# {
#     "system": {
#         "profile": [
#             {
#                 "default-action": "deny-all",
#                 "entry": [
#                     {
#                         "action": "permit",
#                         "match": "back"
#                     },
#                     {
#                         "action": "permit",
#                         "match": "exit"
#                     }
#                 ],
#                 "user-profile-name": "readonly"
#             },
#             {
#                 "default-action": "permit-all",
#                 "entry": [
#                     {
#                         "action": "deny",
#                         "match": "configure system security"
#                     },
#                     {
#                         "action": "permit",
#                         "match": "show system security"
#                     }
#                 ],
#                 "user-profile-name": "administrative"
#             },
#             {
#                 "default-action": "permit-all",
#                 "entry": [
#                     {
#                         "action": "deny",
#                         "match": "configure system security"
#                     },
#                     {
#                         "action": "permit",
#                         "match": "show system security"
#                     }
#                 ],
#                 "user-profile-name": "Test Profile 69"
#             }
#         ]
#     }
# }
# ]"""
#     assert result, profiles


# def test_file_dir_output():

#     """
#     Test parsing file dir output
#     """
#     example_file_dir = "tests/show_output/file_dir.txt"
#     parser = SrosParser(example_file_dir)
#     result = parser.show_file_dir()
#     filedir = """[
# {
#     "cf-contents": {
#         "directory": {
#             "cf-card": "cf3",
#             "count": {
#                 "bytes-free": "789516288",
#                 "bytes-used": "14330",
#                 "total-dirs": "5",
#                 "total-files": "7"
#             },
#             "directories": [
#                 {
#                     "DIR": true,
#                     "date": "11/06/2020",
#                     "directory": ".ssh/",
#                     "time": "06:52a"
#                 },
#                 {
#                     "DIR": true,
#                     "date": "06/17/2020",
#                     "directory": "SYSLINUX/",
#                     "time": "02:06p"
#                 },
#                 {
#                     "DIR": true,
#                     "date": "06/17/2020",
#                     "directory": "TIMOS/",
#                     "time": "02:06p"
#                 },
#                 {
#                     "DIR": true,
#                     "date": "12/30/2020",
#                     "directory": "certs/",
#                     "time": "06:32p"
#                 },
#                 {
#                     "DIR": true,
#                     "date": "11/13/2020",
#                     "directory": "system-pki/",
#                     "time": "02:17a"
#                 }
#             ],
#             "files": [
#                 {
#                     "date": "06/17/2020",
#                     "filename": "CONFIG.CFG",
#                     "size": "0",
#                     "time": "02:06p"
#                 },
#                 {
#                     "date": "06/17/2020",
#                     "filename": "NVRAM.DAT",
#                     "size": "101",
#                     "time": "02:06p"
#                 },
#                 {
#                     "date": "11/14/2020",
#                     "filename": "bof.cfg",
#                     "size": "682",
#                     "time": "02:53a"
#                 },
#                 {
#                     "date": "12/26/2020",
#                     "filename": "bootlog.txt",
#                     "size": "6614",
#                     "time": "02:39p"
#                 },
#                 {
#                     "date": "12/26/2020",
#                     "filename": "bootlog_prev.txt",
#                     "size": "6614",
#                     "time": "02:35p"
#                 },
#                 {
#                     "date": "12/26/2020",
#                     "filename": "nvsys.info",
#                     "size": "317",
#                     "time": "02:38p"
#                 },
#                 {
#                     "date": "12/26/2020",
#                     "filename": "restcntr.txt",
#                     "size": "2",
#                     "time": "02:38p"
#                 }
#             ]
#         },
#         "volume": [
#             {
#                 "slot": "A",
#                 "volume": "in drive cf3 on slot A is SROS VM."
#             },
#             {
#                 "slot": "A",
#                 "volume": "in drive cf3 on slot A is formatted as FAT32"
#             }
#         ]
#     }
# }
# ]"""
#     assert result, filedir


# def test_show_service_service_using():

#     """
#     Test parsing show service service using show command
#     """
#     example_output = "tests/show_output/show_service_service_using.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_service_service_using()
#     services = """[
# {
#     "service-using": {
#         "count": {
#             "total-services": "3"
#         },
#         "services": [
#             {
#                 "admin-state": "Down",
#                 "customer-id": "1",
#                 "operational-state": "Down",
#                 "service-id": "100",
#                 "service-name": "100",
#                 "service-type": "VPRN"
#             },
#             {
#                 "admin-state": "Up",
#                 "customer-id": "1",
#                 "operational-state": "Down",
#                 "service-id": "2147483648",
#                 "service-name": "_tmnx_InternalIesService",
#                 "service-type": "IES"
#             },
#             {
#                 "admin-state": "Up",
#                 "customer-id": "1",
#                 "operational-state": "Down",
#                 "service-id": "2147483649",
#                 "service-name": "_tmnx_InternalVplsService",
#                 "service-type": "intVpls"
#             }
#         ]
#     }
# }
# ]"""
#     assert result, services


# def test_show_router_static_route_tag_ipv4():

#     """
#     Test parsing show router static-route with ipv4 flag
#     """
#     example_output = "tests/show_output/show_router_static_route.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_router_static_route(protocol="IPV4")
#     ipv4_routes = """[
# {
#     "static_route": {
#         "ipv4": {
#             "count": {
#                 "total-routes": "6"
#             },
#             "entry": [
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.115.30.0/24",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.115.43.0/24",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.115.56.0/24",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.119.228.0/23",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.119.228.16/28",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 },
#                 {
#                     "active": "Y",
#                     "ipaddress": "10.253.236.0/23",
#                     "metric": "1",
#                     "next-hop": {
#                         "interface": "n/a",
#                         "next-hop": "n/a"
#                     },
#                     "preference": "5",
#                     "tag": "1000",
#                     "type": "BH"
#                 }
#             ]
#         }
#     }
# }
# ]"""
#     assert result, ipv4_routes


# # def test_show_router_static_route_tag_ipv6():

# #     """
# #     Test parsing show router static-route with ipv6 flag
# #     """
# #     example_output = "tests/show_output/show_router_static_route.txt"
# #     parser = SrosParser(example_output)
# #     result = parser.show_router_static_route(protocol="IPV6")
# #     ipv6_result = """[
# # {
# #     "static_route": {
# #         "ipv6": {
# #             "count": {
# #                 "total-routes": "4"
# #             },
# #             "entry": [
# #                 {
# #                     "active": "Y",
# #                     "ipaddress": "2001:4888:26f:4100::/56",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 },
# #                 {
# #                     "active": "N",
# #                     "ipaddress": "2001:4888:26f:4140::/64",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 },
# #                 {
# #                     "active": "Y",
# #                     "ipaddress": "2001:4888:2000:0:645:2a0::/112",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 },
# #                 {
# #                     "active": "Y",
# #                     "ipaddress": "2001:4888:2062:3000::/52",
# #                     "metric": "1",
# #                     "next-hop": {
# #                         "interface": "n/a",
# #                         "next-hop": "n/a"
# #                     },
# #                     "preference": "5",
# #                     "tag": "1000",
# #                     "type": "BH"
# #                 }
# #             ]
# #         }
# #     }
# # }
# # ]"""
# #     assert result == ipv6_result


# # def test_show_router_route_table():
# #     """Test parsing show router route table."""
# #     # TODO: Convert to fixture
# #     example_output = "tests/show_output/show_router_route_table.txt"
# #     parser = SrosParser(example_output)
# #     result = parser.show_router_route_table()
# #     routes = """[
# # {
# #     "route-table": [
# #         {
# #             "ipv4": {
# #                 "count": {
# #                     "total-routes": "7"
# #                 },
# #                 "entry": [
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.115.30.0/24",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.115.43.0/24",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.115.56.0/24",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m14s",
# #                         "ipaddress": "10.115.56.0/32",
# #                         "next-hop": {
# #                             "metric": "0",
# #                             "next-hop": "system"
# #                         },
# #                         "pref": "0",
# #                         "protocol": "Local",
# #                         "type": "Local"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.119.228.0/23",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.119.228.16/28",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h15m13s",
# #                         "ipaddress": "10.253.236.0/23",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     }
# #                 ]
# #             }
# #         },
# #         {
# #             "ipv6": {
# #                 "count": {
# #                     "total-routes": "4"
# #                 },
# #                 "entry": [
# #                     {
# #                         "age": "09h18m31s",
# #                         "ipaddress": "2001:4888:26f:3100::/56",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h18m31s",
# #                         "ipaddress": "2001:4888:2000:0:645:1a0::/112",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     },
# #                     {
# #                         "age": "09h18m32s",
# #                         "ipaddress": "2001:4888:2000:0:645:1a0::/128",
# #                         "next-hop": {
# #                             "metric": "0",
# #                             "next-hop": "system"
# #                         },
# #                         "pref": "0",
# #                         "protocol": "Local",
# #                         "type": "Local"
# #                     },
# #                     {
# #                         "age": "09h18m31s",
# #                         "ipaddress": "2001:4888:2062:2000::/52",
# #                         "next-hop": {
# #                             "metric": "1",
# #                             "next-hop": "Black Hole"
# #                         },
# #                         "pref": "5",
# #                         "protocol": "Static",
# #                         "type": "Blackh*"
# #                     }
# #                 ]
# #             }
# #         }
# #     ]
# # }
# # ]"""
# #     assert result == routes


# def test_show_ravs_bof():

#     """
#     Test parsing show bof output from RAVS tool
#     """
#     example_output = "tests/show_output/show_ravs_bof.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     ravs_bof1 = """[
#     {
#         "bof": {
#             "address": [
#                 {
#                     "address": "10.202.16.53",
#                     "prefix-length": "23"
#                 },
#                 {
#                     "address": "2001:4888:2A1A:A03D:192:400::1",
#                     "prefix-length": "64"
#                 }
#             ],
#             "config": {
#                 "cf-card": "cf3",
#                 "primary-config": "PHLAPAbts0030.cfg"
#             },
#             "static_route": [
#                 {
#                     "network": "10.134.221.0/24",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.134.240.0/22",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.193.0.0/16",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.194.0.0/16",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "10.215.128.0/17",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "198.226.102.0/24",
#                     "next-hop": "10.202.16.52"
#                 },
#                 {
#                     "network": "199.74.154.0/23",
#                     "next-hop": "10.202.16.52"
#                 }
#             ]
#         }
#     }
# ]"""
#     assert result == ravs_bof1


# def test_show_ravs_bof2():

#     """
#     Test parsing show bof output from RAVS tool
#     """
#     example_output = "tests/show_output/show_ravs_bof2.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     ravs_bof2 = """[
#     {
#         "bof": {
#             "address": [
#                 {
#                     "address": "10.202.16.55",
#                     "prefix-length": "23"
#                 },
#                 {
#                     "address": "2001:4888:2A1A:A03F:192:400::1",
#                     "prefix-length": "64"
#                 }
#             ],
#             "config": {
#                 "cf-card": "cf3",
#                 "primary-config": "PHLAPAbts0032.cfg"
#             },
#             "static_route": [
#                 {
#                     "network": "10.134.221.0/24",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.134.240.0/22",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.193.0.0/16",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.194.0.0/16",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "10.215.128.0/17",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "198.226.102.0/24",
#                     "next-hop": "10.202.16.54"
#                 },
#                 {
#                     "network": "199.74.154.0/23",
#                     "next-hop": "10.202.16.54"
#                 }
#             ]
#         }
#     }
# ]"""
#     assert result == ravs_bof2


# def test_show_ravs_bof2_type():

#     """
#     Test parsing show bof output  1 from RAVS tool -> str
#     """
#     example_output = "tests/show_output/show_ravs_bof2.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     assert type(result) == str


# def test_show_ravs_bof1_type():

#     """
#     Test parsing show bof output 2 from RAVS tool -> str
#     """
#     example_output = "tests/show_output/show_ravs_bof1.txt"
#     parser = SrosParser(example_output)
#     result = parser.show_bof(ravs=True)
#     assert type(result) == str


# def test_get_ports():

#     """
#     Test parsing get ports config
#     """
#     parser = SrosParser(example_config)
#     result = parser.get_ports()
#     output = """[
#     {
#         "configure": {
#             "port": [
#                 {
#                     "admin_state": true,
#                     "description": "7705-MGMT-CSMA",
#                     "ethernet": {
#                         "autonegotiate": false
#                     },
#                     "port-id": "1/5/1"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "BTS0215-1X-URC01",
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "encap-type": "dot1q"
#                     },
#                     "port-id": "1/5/2"
#                 },
#                 {
#                     "admin_state": false,
#                     "ethernet": {},
#                     "port-id": "1/5/3"
#                 },
#                 {
#                     "admin_state": false,
#                     "ethernet": {},
#                     "port-id": "1/5/4"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "LINK-TO-LOOPBACK-7705PORT",
#                     "ethernet": {
#                         "encap-type": "dot1q",
#                         "loopback": true,
#                         "mtu": "2106"
#                     },
#                     "port-id": "1/5/5"
#                 },
#                 {
#                     "admin_state": false,
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "encap-type": "dot1q"
#                     },
#                     "port-id": "1/5/6"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "eNodeB0215-LTE-eCCM01-1",
#                     "ethernet": {
#                         "autonegotiate": "limited",
#                         "encap-type": "dot1q",
#                         "hold-time": {
#                             "down": "50"
#                         },
#                         "mtu": "2106"
#                     },
#                     "port-id": "1/5/7"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "Link-to-TEMPE-AZ-EXAMPLE-P-AL-0415-H1-1/2/8",
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "egress-rate": "96260",
#                         "encap-type": "dot1q",
#                         "hold-time": {
#                             "down": "25",
#                             "up": "50"
#                         },
#                         "mode": "network",
#                         "mtu": "2106"
#                     },
#                     "port-id": "1/5/8"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "7705-MGMT-CSMB",
#                     "ethernet": {
#                         "autonegotiate": false
#                     },
#                     "port-id": "1/6/1"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "BTS0215-1X-URC02",
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "encap-type": "dot1q"
#                     },
#                     "port-id": "1/6/2"
#                 },
#                 {
#                     "admin_state": false,
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "encap-type": "dot1q"
#                     },
#                     "port-id": "1/6/3"
#                 },
#                 {
#                     "admin_state": false,
#                     "ethernet": {},
#                     "port-id": "1/6/4"
#                 },
#                 {
#                     "admin_state": false,
#                     "ethernet": {},
#                     "port-id": "1/6/5"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "BTS0215-DO-URC03",
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "encap-type": "dot1q"
#                     },
#                     "port-id": "1/6/6"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "eNodeB324215-LTE-eCCM01-1",
#                     "ethernet": {
#                         "autonegotiate": "limited",
#                         "encap-type": "dot1q",
#                         "hold-time": {
#                             "down": "50"
#                         },
#                         "mtu": "2106"
#                     },
#                     "port-id": "1/6/7"
#                 },
#                 {
#                     "admin_state": true,
#                     "description": "Link-to-TEMPE-AZ-EXAMPLE-P-AL-0415-H2-1/2/8",
#                     "ethernet": {
#                         "autonegotiate": false,
#                         "egress-rate": "96260",
#                         "encap-type": "dot1q",
#                         "mode": "network",
#                         "mtu": "2106"
#                     },
#                     "port-id": "1/6/8"
#                 }
#             ]
#         }
#     }
# ]"""
#     assert output == result


# def test_get_log_configuration():

#     """
#     Test parsing log configuration
#     """
#     parser = SrosParser(example_config)
#     result = parser.get_log_configuraiton()
#     log = """[
#     {
#         "configure": {
#             "log": [
#                 {
#                     "file": [
#                         {
#                             "file-id": "10"
#                         },
#                         {
#                             "compact-flash-location": {
#                                 "primary": "cf3"
#                             },
#                             "description": "Syslog-storage",
#                             "file-id": "20",
#                             "retention": "350",
#                             "rollover": "1440"
#                         },
#                         {
#                             "compact-flash-location": {
#                                 "primary": "cf3"
#                             },
#                             "description": "Change-storage",
#                             "file-id": "30",
#                             "retention": "350",
#                             "rollover": "1440"
#                         }
#                     ],
#                     "log-events": {
#                         "chassis": [
#                             {
#                                 "event": "system",
#                                 "event-id": "2103",
#                                 "generate": true
#                             },
#                             {
#                                 "event": "system",
#                                 "event-id": "2104",
#                                 "generate": true
#                             },
#                             {
#                                 "event": "vrtr",
#                                 "event-id": "2034",
#                                 "generate": true
#                             }
#                         ]
#                     },
#                     "snmp-trap-group": [
#                         {
#                             "log-id": "10"
#                         },
#                         {
#                             "log-id": "7",
#                             "trap-target": {
#                                 "address": "10.141.128.78",
#                                 "name": "SW_INC",
#                                 "notify-community": "2Y2LHTZP31",
#                                 "snmp-version": "snmpv2c"
#                             }
#                         },
#                         {
#                             "description": "5620sam",
#                             "log-id": "98",
#                             "trap-target": [
#                                 {
#                                     "address": "99.194.69.164",
#                                     "name": "0017A4770C06:main1",
#                                     "notify-community": "snmpuser3",
#                                     "security-level": "privacy",
#                                     "snmp-version": "snmpv3"
#                                 },
#                                 {
#                                     "address": "99.215.238.164",
#                                     "name": "0017A4770C06:main2",
#                                     "notify-community": "snmpuser3",
#                                     "security-level": "privacy",
#                                     "snmp-version": "snmpv3"
#                                 },
#                                 {
#                                     "address": "99.194.69.164",
#                                     "name": "99.194.69.164:162",
#                                     "notify-community": "snmpuser3",
#                                     "security-level": "privacy",
#                                     "snmp-version": "snmpv3"
#                                 },
#                                 {
#                                     "address": "99.215.238.164",
#                                     "name": "99.215.238.164:162",
#                                     "notify-community": "snmpuser3",
#                                     "security-level": "privacy",
#                                     "snmp-version": "snmpv3"
#                                 }
#                             ]
#                         }
#                     ],
#                     "syslog": {
#                         "address": "10.215.141.147",
#                         "description": "Syslog Server",
#                         "syslog-id": "5"
#                     }
#                 },
#                 {
#                     "log-id": "5",
#                     "source": {
#                         "change": true,
#                         "main": true,
#                         "security": true,
#                         "source": "main"
#                     }
#                 },
#                 {
#                     "description": "SW_INC",
#                     "destination": "snmp",
#                     "log-id": "7",
#                     "source": {
#                         "main": true,
#                         "security": true,
#                         "source": "main"
#                     }
#                 },
#                 {
#                     "log-id": "20",
#                     "source": {
#                         "main": true,
#                         "security": true,
#                         "source": "main"
#                     }
#                 },
#                 {
#                     "log-id": "30",
#                     "source": {
#                         "change": true,
#                         "source": "change"
#                     }
#                 },
#                 {
#                     "log-id": "98",
#                     "source": {
#                         "main": true,
#                         "security": true,
#                         "source": "main"
#                     }
#                 }
#             ]
#         }
#     }
# ]"""
#     assert log == result