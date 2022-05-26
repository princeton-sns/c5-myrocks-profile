"""CloudLab profile for C5-MyRocks experiments"""


import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.emulab as emulab

# Constants
image = 'urn:publicid:IDN+wisc.cloudlab.us+image+cops-PG0:multicore-replication:3'

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node client
node_client = request.RawPC('client')
node_client.disk_image = image
node_client.hardware_type = 'c220g5'
iface0 = node_client.addInterface('interface-0')
bs = node_client.Blockstore("bs-client", "/data")
bs.size = "128GB"
bs.placement = "sysvol"

# Node primary
node_primary = request.RawPC('primary')
node_primary.disk_image = image
node_primary.hardware_type = 'c220g5'
iface1 = node_primary.addInterface('interface-1')
bs = node_primary.Blockstore("bs-primary", "/data")
bs.size = "128GB"
bs.placement = "sysvol"

# Node backup
node_backup = request.RawPC('backup')
node_backup.disk_image = image
node_backup.hardware_type = 'c220g5'
iface2 = node_backup.addInterface('interface-2')
bs = node_backup.Blockstore("bs-backup", "/data")
bs.size = "128GB"
bs.placement = "sysvol"

# Link link-0
link_0 = request.Link('link-0')
link_0.Site('undefined')
link_0.addInterface(iface2)
link_0.addInterface(iface1)
link_0.addInterface(iface0)


# Print the generated rspec
pc.printRequestRSpec(request)
