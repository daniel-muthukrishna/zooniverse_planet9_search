"""- We will need to know the date, time of the image too when an object is detected.
All of the data is here:/data/motley1/brad/P9.
If you look up a field, take field 99, you can see the various files and input.
We’ll need some sort of wrapper to get the date and time from the image (it is in the file name),
and use that all together."""



def get_date_time(field):
    """ Takes field as a string e.g. field='99' """
    fieldInfo = {'8097': '2014-06-28T20:56:25', '8096': '2015-05-24T22:46:36', '8095': '2015-05-24T22:38:54', '8093': '2015-05-22T22:30:18', '1943': '2015-08-16T01:02:20', '1946': '2014-11-22T23:23:41', '1947': '2015-08-09T03:32:15', '1944': '2015-08-27T00:51:31', '1945': '2014-11-19T23:45:30', '1799': '2015-08-19T00:56:37', '4111': '2014-10-20T01:39:21', '1793': '2015-06-25T02:37:31', '1792': '2015-09-14T20:53:28', '1791': '2015-08-08T03:10:05', '1797': '2015-08-16T00:49:57', '1796': '2015-06-28T02:26:11', '1795': '2015-09-10T21:39:27', '710': '2015-06-12T20:53:03', '1490': '2015-07-09T23:10:36', '4114': '2014-09-21T02:53:33', '2315': '2015-08-22T20:42:55', '1065': '2015-09-13T22:43:37', '1067': '2015-06-21T02:28:57', '1066': '2015-09-20T21:51:59', '1665': '2015-09-19T23:56:50', '1664': '2015-06-29T05:28:14', '1907': '2015-05-23T01:12:09', '3384': '2014-11-22T02:36:42', '3383': '2014-11-20T03:06:49', '2385': '2015-12-18T04:07:21', '2384': '2015-12-17T04:09:54', '1401': '2014-11-27T23:26:19', '3589': '2016-03-19T21:11:32', '4193': '2014-06-22T21:19:12', '102': '2015-05-23T00:35:53', '103': '2014-06-18T00:15:43', '100': '2015-05-23T00:47:56', '101': '2015-06-06T21:37:08', '1933': '2015-09-10T21:59:33', '39': '2014-11-22T04:13:32', '31': '2014-11-22T01:47:53', '30': '2014-11-22T01:39:05', '36': '2014-10-30T04:27:11', '35': '2014-11-20T04:14:20', '1536': '2014-11-16T02:05:54', '4115': '2014-10-21T02:17:37', '1247': '2015-12-14T23:07:30', '1246': '2015-12-14T23:27:56', '1936': '2015-09-06T22:56:33', '3806': '2015-07-09T23:48:43', '2619': '2015-12-17T04:05:51', '4101': '2014-10-20T00:13:22', '4100': '2014-10-19T23:49:18', '4103': '2014-09-21T01:17:13', '4102': '2014-09-05T02:14:42', '4105': '2014-09-06T02:33:30', '4104': '2014-10-20T00:37:27', '4107': '2014-09-06T02:55:13', '1909': '2015-05-27T01:39:12', '4109': '2014-09-08T02:57:59', '4108': '2014-10-05T01:12:17', '3457': '2015-12-07T01:57:19', '3459': '2014-11-22T03:17:13', '8024': '2014-10-21T03:21:54', '2688': '2014-10-03T20:50:32', '2689': '2014-09-20T23:27:40', '6': '2014-09-04T02:16:31', '1469': '2015-05-24T02:11:12', '547': '2016-04-15T23:15:11', '99': '2015-06-06T21:20:47', '98': '2015-06-06T21:12:16', '91': '2015-07-07T19:44:47', '90': '2015-05-14T22:34:37', '93': '2015-05-22T22:26:18', '95': '2015-05-22T22:42:19', '94': '2014-06-17T20:57:00', '97': '2016-03-15T04:50:35', '96': '2014-07-03T20:40:02', '4175': '2016-03-02T02:40:38', '4177': '2016-03-02T03:59:45', '1997': '2016-02-29T23:20:39', '1996': '2016-03-03T23:00:00', '1629': '2015-05-25T03:57:34', '2867': '2015-07-21T19:44:20', '555': '2015-06-13T20:28:15', '551': '2015-05-13T23:26:45', '553': '2015-05-23T21:57:54', '552': '2015-05-14T22:10:53', '238': '2016-03-06T01:49:58', '239': '2016-03-04T02:56:31', '234': '2015-05-09T21:10:35', '231': '2015-05-09T20:50:32', '233': '2015-05-23T20:16:56', '1198': '2015-06-22T23:47:36', '3348': '2014-06-23T00:29:06', '1057': '2014-09-01T20:09:35', '1193': '2015-06-08T23:34:54', '1195': '2015-05-25T03:53:34', '1194': '2015-06-11T01:44:02', '1197': '2015-07-09T23:31:22', '1196': '2015-06-20T23:55:23', '1': '2014-09-05T01:42:27', '1754': '2015-05-16T01:25:51', '1177': '2015-05-27T00:44:39', '1176': '2015-05-24T00:18:26', '1175': '2014-06-30T19:09:02', '145': '2014-07-04T04:46:21', '143': '2014-07-02T03:39:33', '612': '2014-10-22T22:44:23', '613': '2014-10-22T22:11:55', '610': '2015-06-23T03:54:59', '611': '2014-10-27T22:17:27', '148': '2014-10-20T22:12:44', '1889': '2014-07-03T19:38:56', '1794': '2015-06-29T02:10:09', '1881': '2015-05-23T20:42:02', '1880': '2015-07-05T21:08:26', '80': '2016-03-02T04:19:52', '1470': '2015-05-24T00:38:30', '8018': '2014-09-06T03:57:55', '8017': '2014-10-21T01:45:31', '8016': '2014-09-21T02:35:30', '139': '2014-09-03T22:40:41', '8014': '2014-10-21T01:13:23', '8011': '2014-10-20T01:01:30', '493': '2015-12-17T00:58:22', '24': '2014-10-21T02:49:43', '27': '2014-11-22T01:12:12', '20': '2014-10-06T03:07:41', '22': '2014-10-06T03:27:45', '23': '2014-10-06T03:50:30', '8026': '2014-10-19T03:50:53', '3791': '2016-04-13T19:21:08', '29': '2014-11-22T01:29:31', '938': '2014-09-08T03:06:01', '402': '2015-06-20T20:08:08', '400': '2015-06-20T20:03:03', '2847': '2016-03-27T00:39:22', '1344': '2015-07-09T23:36:15', '455': '2015-06-22T03:24:11', '1954': '2014-10-29T00:31:17', '1957': '2014-10-30T03:50:49', '1956': '2014-11-21T23:32:36', '1950': '2015-08-28T01:41:07', '1959': '2014-10-30T03:30:44', '1958': '2014-11-12T03:22:19', '709': '2015-07-09T20:03:49', '393': '2016-03-03T03:46:42', '392': '2016-04-27T21:19:49', '88': '2015-05-23T21:40:47', '89': '2015-05-12T22:31:37', '1487': '2015-06-13T00:36:57', '1486': '2015-06-13T01:54:36', '394': '2016-04-03T01:27:21', '1489': '2015-07-09T22:37:20', '1488': '2015-06-22T00:11:49', '86': '2015-05-13T23:18:42', '3303': '2014-11-22T02:16:37', '84': '2015-05-11T21:50:06', '4251': '2014-08-29T01:42:46', '7': '2014-09-21T01:05:04', '1631': '2015-06-12T23:36:24', '589': '2016-03-28T05:38:11', '245': '2015-06-06T20:38:42', '244': '2015-05-24T21:41:26', '247': '2015-05-24T22:16:12', '246': '2015-05-12T22:51:40', '241': '2015-05-24T21:13:30', '243': '2015-06-10T22:13:43', '242': '2015-06-20T19:27:19', '249': '2015-05-14T23:14:45', '248': '2015-06-07T21:15:14', '2277': '2015-06-09T22:15:43', '2574': '2014-10-03T21:06:45', '2573': '2014-09-20T22:21:55', '514': '2015-12-20T01:55:22', '458': '2014-10-21T22:03:13', '459': '2014-10-21T22:23:38', '1340': '2015-06-20T23:11:39', '1342': '2015-06-20T23:03:38', '1343': '2015-07-19T22:04:55', '454': '2014-10-22T21:27:46', '1345': '2015-07-09T00:31:53', '456': '2014-10-23T21:39:34', '457': '2014-10-21T21:47:07', '1879': '2015-07-05T21:36:46', '183': '2014-11-23T01:25:48', '2': '2014-10-19T23:45:17', '186': '2014-11-23T01:41:52', '187': '2014-11-29T01:42:53', '185': '2014-11-20T01:57:35', '399': '2015-05-23T21:49:53', '2620': '2015-12-30T01:59:19', '2621': '2016-03-19T21:15:33', '1911': '2015-07-09T22:17:48', '1910': '2015-06-20T22:59:19', '1912': '2015-05-23T01:33:44', '11': '2014-08-29T03:16:15', '10': '2014-09-01T03:05:24', '13': '2014-09-06T03:04:55', '12': '2014-09-04T03:36:29', '15': '2014-09-06T03:33:51', '14': '2014-08-29T03:50:28', '17': '2014-09-06T03:49:54', '16': '2014-09-01T03:53:39', '19': '2014-09-01T04:25:53', '18': '2014-08-29T04:31:33', '862': '2015-06-14T20:28:02', '2759': '2015-07-20T20:19:14', '3302': '2014-11-28T00:30:22', '1968': '2014-11-19T01:23:21', '1966': '2014-11-20T04:12:20', '1967': '2014-11-20T04:08:18', '1960': '2014-10-06T01:38:31', '1613': '2015-05-24T00:58:35', '1962': '2014-11-21T00:05:57', '1963': '2014-11-22T00:13:25', '205': '2015-12-20T00:55:48', '77': '2016-03-06T01:25:16', '75': '2016-03-27T22:52:09', '70': '2015-05-13T20:17:01', '78': '2015-05-13T20:42:48', '1594': '2015-05-23T19:30:24', '1681': '2014-10-19T00:28:48', '1680': '2014-09-08T01:56:34', '1685': '2014-11-20T23:53:52', '1684': '2014-10-29T03:35:36', '1687': '2014-10-22T04:29:49', '1686': '2014-11-21T23:57:21', '8155': '2014-10-19T23:13:09', '8153': '2014-10-19T22:49:03', '8150': '2014-10-21T22:19:37', '8151': '2015-06-21T05:26:20', '3079': '2015-08-16T20:15:11', '1544': '2014-11-19T02:26:30', '546': '2016-04-27T21:14:42', '1468': '2015-05-15T00:54:23', '545': '2016-04-14T21:31:40', '8': '2014-09-01T02:57:22', '548': '2016-03-04T03:00:35', '549': '2016-04-15T23:10:31', '125': '2014-09-01T21:03:35', '4238': '2014-08-27T23:46:28', '4237': '2014-10-20T20:56:10', '4235': '2014-10-19T20:50:21', '4233': '2014-09-01T23:30:11', '4231': '2014-08-28T22:37:08', '8025': '2014-10-20T03:19:47', '1828': '2014-11-22T00:26:17', '1821': '2014-10-19T00:48:51', '1820': '2014-09-06T02:17:26', '1823': '2014-11-13T02:22:59', '1822': '2014-11-20T23:45:49', '1579': '2016-03-06T23:33:14', '1948': '2015-08-10T03:38:32', '1926': '2015-08-11T22:47:14', '1927': '2015-08-13T22:41:39', '1928': '2015-08-13T23:59:43', '1929': '2015-09-04T22:06:14', '8015': '2014-10-19T01:49:55', '4122': '2014-10-20T03:39:54', '4121': '2014-10-21T03:01:47', '4120': '2014-10-20T04:24:04', '3': '2014-09-01T01:56:57', '360': '2016-03-01T22:25:04', '389': '2016-03-06T01:57:58', '780': '2014-11-22T22:54:48', '1722': '2016-04-01T01:31:00', '1723': '2016-04-13T19:49:28', '1721': '2016-02-29T23:00:31', '150': '2014-07-04T05:14:28', '28': '2014-11-23T01:17:01', '3790': '2015-12-06T03:51:03', '252': '2015-05-24T22:55:30', '69': '2015-05-16T19:05:42', '250': '2015-06-10T21:09:58', '251': '2015-05-26T23:47:35', '257': '2015-05-23T00:39:53', '255': '2015-05-23T23:38:18', '1580': '2016-03-15T21:36:41', '1581': '2016-03-04T01:46:59', '500': '2015-12-19T00:26:37', '1213': '2014-10-22T21:18:55', '1214': '2015-06-21T05:24:20', '4242': '2014-09-01T00:52:00', '1612': '2015-05-24T01:51:09', '8060': '2016-02-28T21:50:08', '608': '2014-10-23T21:19:31', '1861': '2016-03-15T21:40:41', '1860': '2016-03-01T22:38:52', '1862': '2016-04-14T22:16:04', '1456': '2015-07-06T21:27:39', '1457': '2015-07-05T21:32:44', '1450': '2015-05-16T21:53:31', '1458': '2015-05-24T20:21:21', '2733': '2015-12-18T04:03:20', '4243': '2014-10-20T21:48:39', '1816': '2015-09-07T04:46:06', '1813': '2015-08-10T03:58:40', '1819': '2014-11-20T23:00:22', '3768': '2015-07-28T20:27:26', '9': '2014-09-01T02:53:21', '8145': '2014-10-19T21:40:46', '1601': '2015-05-22T21:17:04', '1600': '2015-05-13T20:58:54', '1602': '2015-06-10T21:41:29', '1538': '2014-11-14T23:54:19', '1614': '2015-05-13T01:53:35', '359': '2015-12-17T02:33:21', '358': '2015-12-31T00:09:21', '1789': '2015-08-11T22:55:58', '763': '2015-09-04T22:47:18', '766': '2014-10-23T23:01:55', '764': '2015-06-28T02:17:23', '1774': '2015-05-23T01:29:20', '1771': '2015-06-08T23:26:53', '1770': '2015-05-23T01:16:49', '1773': '2015-07-09T22:12:47', '1772': '2015-06-20T22:55:17', '1076': '2014-09-05T02:02:34', '1679': '2014-11-22T01:04:03', '8149': '2014-09-01T00:47:58', '1095': '2015-12-14T22:47:00', '1097': '2015-12-02T23:36:08', '1159': '2016-04-12T22:12:48', '1158': '2016-04-01T01:10:37', '8141': '2014-10-19T21:20:42', '3769': '2015-07-19T23:26:11', '8143': '2014-08-28T23:49:25', '8142': '2014-10-18T21:27:18', '1098': '2015-12-07T23:50:03', '8144': '2015-08-17T00:26:32', '8147': '2015-06-15T05:14:46', '8146': '2014-10-19T22:00:52', '59': '2016-02-29T21:27:03', '50': '2016-01-01T00:22:06', '52': '2015-12-20T00:59:48', '2394': '2015-05-23T19:51:23', '1323': '2015-05-23T01:04:06', '1324': '2015-05-27T00:52:39', '1325': '2015-05-27T00:40:39', '8138': '2014-10-18T20:47:09', '8139': '2015-06-28T03:28:44', '253': '2015-05-26T23:03:08', '8135': '2015-05-27T04:41:50', '8136': '2015-06-10T01:56:17', '8137': '2015-06-28T03:48:52', '918': '2014-10-27T22:52:09', '915': '2015-09-14T22:47:09', '914': '2015-08-11T00:30:05', '1392': '2015-12-08T00:10:08', '913': '2015-08-12T00:16:50', '307': '2014-08-29T01:14:40', '4116': '2014-10-19T02:30:35', '1932': '2014-10-28T20:55:03', '1931': '2015-06-25T02:57:32', '1930': '2015-08-09T02:36:26', '4112': '2014-09-05T03:35:05', '4113': '2014-10-20T02:19:33', '4110': '2014-09-01T03:37:36', '1934': '2015-09-10T01:30:29', '4118': '2014-10-19T02:50:40', '2674': '2015-09-04T20:45:26', '1630': '2015-05-24T04:14:20', '3215': '2015-12-05T00:47:54', '1632': '2015-06-22T23:13:41', '1633': '2015-07-09T22:32:48', '1634': '2015-05-23T01:37:44', '8148': '2015-06-22T03:16:07', '1735': '2015-05-23T19:25:52', '1734': '2015-05-12T19:12:22', '1737': '2015-06-05T22:13:39', '1736': '2015-05-23T19:34:26', '1595': '2015-05-24T19:33:10', '3071': '2015-07-19T19:37:41', '1593': '2015-05-23T19:14:28', '226': '2015-05-15T19:27:28', '224': '2015-05-12T19:33:23', '3177': '2015-08-16T21:24:11', '1027': '2015-05-25T00:22:32', '1028': '2015-05-16T01:05:44', '3217': '2015-12-07T01:49:09', '1740': '2015-05-23T20:24:57', '1741': '2015-07-06T21:11:37', '1742': '2015-07-05T21:12:41', '1743': '2015-06-10T21:45:30', '151': '2014-10-20T22:45:10', '8078': '2015-05-23T20:08:48', '153': '2014-08-29T01:34:43', '152': '2014-07-02T04:59:39', '155': '2014-08-29T01:58:49', '4249': '2014-09-04T02:12:14', '4246': '2014-08-28T01:01:14', '4247': '2014-10-20T22:49:11', '8073': '2016-03-27T00:56:05', '609': '2015-08-21T00:10:09', '8074': '2016-03-06T00:26:54', '8077': '2015-05-13T20:33:55', '1894': '2014-07-03T19:34:55', '1897': '2016-04-19T04:10:12', '1891': '2014-07-03T19:26:05', '1892': '2015-05-16T01:45:54', '81': '2014-05-30T21:08:34', '49': '2015-12-07T02:57:57', '47': '2015-12-31T00:04:41', '45': '2015-12-30T23:45:10', '5': '2014-09-01T02:29:14', '3300': '2016-02-29T21:39:39', '1449': '2015-05-22T21:09:00', '4097': '2014-10-19T23:25:11', '4099': '2014-09-01T02:00:59', '8004': '2014-10-20T23:47:26', '8005': '2015-09-13T00:50:01', '8006': '2015-06-28T05:31:04', '8007': '2015-09-19T23:07:26', '8001': '2015-09-12T22:58:28', '8002': '2015-09-12T23:02:50', '8003': '2014-10-19T23:41:15', '1807': '2015-08-27T00:30:51', '1805': '2015-06-29T05:32:36', '1809': '2014-11-12T00:02:37', '1808': '2014-10-28T22:55:36', '2008': '2016-03-21T02:41:28'}

    return fieldInfo[field]

print(get_date_time('12'))


###### CREATE fieldInfo LIST ARRAY ######
# import os
# rootdir = '.'
#
# info = {}
#
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         if 'raw' in subdir:
#             field = subdir.split('/')[1]
#             datetime = file.split('_')[2]
#             info[field] = datetime
#             # info.append([int(field), datetime])
#             break
#
# #sortedInfo = sorted(info,key=lambda x: (x[0]))
# #print sortedInfo
#
# print(info)