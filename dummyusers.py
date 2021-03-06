from bigchaindb import Bigchain
import writeout

b = Bigchain()

# create 7 test users
testuser1_priv, testuser1_pub = b.generate_keys()
writeout.exportData((testuser1_priv, testuser1_pub), "user1")

testuser2_priv, testuser2_pub = b.generate_keys()
writeout.exportData((testuser2_priv, testuser2_pub), "user2")

testuser3_priv, testuser3_pub = b.generate_keys()
writeout.exportData((testuser3_priv, testuser3_pub), "user3")

testuser4_priv, testuser4_pub = b.generate_keys()
writeout.exportData((testuser4_priv, testuser4_pub), "user4")

testuser5_priv, testuser5_pub = b.generate_keys()
writeout.exportData((testuser5_priv, testuser5_pub), "user5")

testuser6_priv, testuser6_pub = b.generate_keys()
writeout.exportData((testuser6_priv, testuser6_pub), "user6")

testuser7_priv, testuser7_pub = b.generate_keys()
writeout.exportData((testuser7_priv, testuser7_pub), "govt")
