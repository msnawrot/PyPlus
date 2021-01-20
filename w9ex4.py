from my_devices import nxos1
from my_functions import open_napalm_connection, create_checkpoint

# Create a Python script that stages a complete configuration replace operation
# (using the checkpoint file that you just retrieved and modified).
print("Opening connection")
conn = open_napalm_connection(nxos1)
print("Loading candidate config (replace)")
conn.load_replace_candidate(filename="nxos1.lasthop.io-new_checkpoint.txt")

# Once your candidate configuration is staged perform a compare_config (diff) on
# the configuration to see your pending changes.
print("CONFIG DIFF:")
print(conn.compare_config())
input("Press any key to continue.")

# After the compare_config is complete, then use the discard_config() method to
# eliminate the pending changes.
print("Discarding candidate config")
conn.discard_config()

# Next, perform an additional compare_config (diff) to verify that you have no
# pending configuration changes.
# Do not actually perform the commit_config as part of this exercise
print("Verifying no changes to config")
print(conn.compare_config())
print("Any config diffs would appear in the line above")
