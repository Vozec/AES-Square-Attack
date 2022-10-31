from binascii import hexlify,unhexlify

from SquareAttack import *

cts = [b'7469e6431d6db86964f811c242be7899', b'c28abdb050daee2d4ed10d0848104d11', b'74c7a6eed81aa775c14cddf1a1b06c89', b'26f88b6fe536c3adf1245a18ca64c106', b'798500dacd3942b2d5646b83ccebc345', b'990cb1746d39cdcf436515ac41400fc5', b'1e37b437f328810192e0ed67360b8b54', b'efbf073fbf36848be88fd9d3c082a83d', b'a5f2d099727243e546fdc3437cbdfb0b', b'1695e928775add7e64fea41c4791f545', b'bebcabba04a15e281b46bc7ce7c22d6b', b'6a2adc36720f351f0cc1ad18e9724a08', b'2c58e80da2c15fd044ad75b8e658e67b', b'1e39359f8af813331807bb874f031951', b'22bdc0528a30fda1e550b56c607d51d6', b'6bae869483f1660a99b133fbb61c8caa', b'ab95ef26bdfce0dfef2895289ffba0e3', b'c9b208c0e035f818e9209829f5f57e12', b'a286108e1883039cd63441d551b731fb', b'72cfc78b512e305206e898b3a70a63bf', b'f9d83ab8bad9ad6475c271941316a768', b'2249bce1d2e115f1d94a807f9932a84c', b'bda7bdfa02ee86ceec1e981f821a125a', b'30bd099e65b838d12a44da307d5e30ae', b'907935b577780441f5ee152f727f5324', b'742e4e41e30202dd1c346fe9d34bf79d', b'7ba4585540bcf68af2eede7dda69afb6', b'7277222f7dc6822627f525d678a9319d', b'71e0b2a766795b1506f869e01915b718', b'7499aa194575bf4748cc3a65b010e8b6', b'ba3d01e9e64ce39219df28698152f0cc', b'24f60fa5c2a9cf4b7e82d1aa79cf8a7c', b'0fc4e5aeabe1f55c5c4b30a4b93b3cb1', b'5faec681e7ad9026279fb16646496840', b'dc1ead876257043a711fd5611c7e73a0', b'ce25be571c645066b4757595d80d89cd', b'5df04f2dd145b925de6f68ae7becf684', b'4b117c58853e81876ea47b97fe031fcc', b'606f9b577d313cb4114725a0a88506aa', b'ef168f6391251e42d87217accbf6985b', b'4e8784f73a1345822f1e9703c7eabe18', b'19289b36dbea7267fc4b582378042eb1', b'818e94982e43b586ee3ba00b5b257e3e', b'a6bcfc90df7ace1ef9aa67582bf76a20', b'f835a9a6545d23bbeddf001d297b39b1', b'a536e499cd23b3ada46ff64379f66174', b'f50798d533eedf1f67c1a124e1d34f9c', b'ba36b01c3d387a99a7419c2eb2d1a087', b'88b41c0fb9201d8c65b201a127c56fc5', b'706b220a36bf1954278c828006fcbee7', b'217517aa7c9bf1c0f9a0b84c0cdd54c0', b'3d3b097b9999170b09e25a0e801ea193', b'41bb929954516ab1e371ba83fbeefe62', b'11b307927ced308ef05deb0748eabac3', b'5863fe7fc1af036f1b00c1a0e8e3ded5', b'73c5fc3078b3019bffc9de4d3c480c56', b'ad0b4ac585e5e96637d93cfc629be047', b'a26a0e7e277481274e01d819450ccf5f', b'dd8a140c7fb84cca688cf3e311252b68', b'a53904e8313ac20242aa2d9adb8bb648', b'61d41da1746b4c6095cc12eed63bb70b', b'9863e84a5b0da7312992794d9106c11e', b'a35ebee0bf6f3f57f7fd11a5cb87ad6e', b'a74842441fec7f43b4690ffb2f383da9', b'b298ff8d160ecdf7796c2ba807550bce', b'4d9b3948aa74530cc1ad8db5b7bfd829', b'726989f9ad7f88bef513ce584f4ff53a', b'1c33f07ee69aff09ebd30827fda9a95e', b'0974a34228a436d35151299dd2255760', b'3019b37b7c82edde613acbc2a4b3e254', b'37811ac90cf122c7201a0d10379fd0cd', b'e08afbe5216b877c1df68b004a033fa4', b'a6506e1f987a8e7b188b17d9ebedc323', b'64853df79818b4ff8435d891a2057f0f', b'9c64e77b4ef5279c9f1f66fcacdfe2a6', b'a07f7e74bbad15d92084bf8083fa290e', b'1db0c0c979e266a894c61eb9a8bc5130', b'aad529c5e823818fc0bdf7052d81467b', b'211b035a79bb03079a0b0e1e3760a186', b'953e2f58104bdb7aff58965cb4380e93', b'a792b098a24fbf6cd1993429c53b736b', b'96b4bc35d6146ebe24fccc4492d4f68d', b'62c5bdacca0db11b3d59c81b56fb6498', b'6779ac3829673aed24d6a2472b4cd984', b'1c47a17706f13916b99e1abf9cbec092', b'6292ecb22f921033d23ff91d7a713d6e', b'40580b260b423d618cd4a05768d2c538', b'8ed76c2a61cfb0926cd189103f4647bc', b'e10cfc910f7c955366c95914ed293690', b'd5d497ab4f8c0cc7f89e4f7d88326d12', b'bbfc5d4d87646b8241bb9146102962b4', b'3d245eea323467fcd8943c6e97c6b125', b'fbb4ed49ba179c7d7a5936af329e2b53', b'da250fbcf60473ade83035eb1d08fdb6', b'101a4a2d65984f346141b134990c44e8', b'1d88fc5934d22b43256448b1326272e0', b'6c86b2ce2beca2a3322089c004464b72', b'1b126d75559e232a34b9203cbd43f323', b'90665455c6fb34c8d5b91c4e53db2a69', b'a654084c983cb11517170e7e2c33246f', b'0098145da08a01e7024ec64a7e428784', b'00e86b603e154a2a4b04c3d51b41a512', b'd84c83b9b298d24996364cca7ccba593', b'd5c90885fd14f48e9076714d5969dc02', b'427b6fb2d857adb136a26ab70e1a4b07', b'aa7f5b10dcb310f202df1f9762f39d80', b'8cfb0bc9a68a039ed0d0eb3f2aad0963', b'5c05dad0cbea72a308042c7b405fa13c', b'be8b1bd5fc9124b55882c78d23a2c8c0', b'd3bd444546967b67ac0cc642c62721de', b'28cbb0fa118bd3f53f0d82dad5fcaa27', b'1bd1bb2bb9439572b6e09894f0c84f1f', b'0e828424fa80478555b0978f56ed13f2', b'c361f985696e75786ae66852ac409c6b', b'2a7dd99dd5ad9347eaed518776dc108e', b'02c834b04d049285f8fc48be10015333', b'762e49df4776524b23a36c02d15dc94e', b'01559303c2fc8de5c6d4de6fae5d42de', b'2bf8cbdc1de695fe7ca91894e4d23520', b'e21190c5b5ac6ed1256efc57cd447928', b'4b03c2c5ed7cc87e22b1647ef6cb821f', b'e50025dfdd1e1dbaf56f11bfe68e3dff', b'bc315638a93d91e1b2a8f5d2a7380129', b'70c8f7c714e557811e323d35a74df63e', b'd47556d5bc9f1430ec0bc2d8b37c3cd9', b'fecaca6590b720cbadcab2a0c5124d3f', b'e52cc84f7ed10701a93e928fdaa92c64', b'354bee582e37dca5bc4731c60c04f1ce', b'd2de74a9e610ac14881abf693fabc995', b'fbd4e6c49c928dc59850c30a2939100d', b'bb88ced9b04c97ac140868b49a0e492b', b'e69afc94ba2c2ead6829e2f65ecf5e74', b'5e215719c60f6e96ac44fdc733ed984b', b'990ba18f39406156715975a7a580d2e9', b'bf84a2d309082608b1bbf5ee9b93523a', b'05bb3ce6ff4644e86f0e45b690d04082', b'5cf6c6f8257ff7a72fa01bdd91539129', b'c064ee808c000912f704d4da9ba33fc2', b'0dc13a75ceb5937f34fe5098f500eaa8', b'b80b2012019486b59e12df75b80aa4d2', b'4c0e907e8bb3958275ab09ea97abd25c', b'833ea3eba9a55dcbe692bacdfaf75fe7', b'a5ac2146849abfe2a9d74c9f264a35be', b'f2ad3eeaae25697fad83dbbf35b2b6ea', b'5f4c9d32c54fa7522af20c511e85134c', b'c804128f6e41568bca86f80e0b558aa5', b'b2ee11c37179bc4e5a8ab7ce6d4aa796', b'62e979fc2177efc834df81c9accb401c', b'e6ebb42efe5cd2c782658b51c0f83a04', b'6c324762cadb4db49b25180e830d680e', b'32c18e2b383e8fd4ece7938da5a0f7da', b'38df40497deec62dbaed8e6b3cb40817', b'455f6317f03f422924ec4ca8f892ce3b', b'7f7c5e55cb67554ecf160a62cb2ac18e', b'4e71158adee0779dc39f6febb8faaec7', b'acc9838e1dacabe2e34f49009cfa570b', b'925f40ca39850f28eeba1c98a28bcb00', b'2c51bd29760d7da6f5f48edf4a8dda2d', b'7bcdc5ea77487541e1300faec8751393', b'fdf9ded59e2e118530d6d08a236e61da', b'693d27b39d400a88f2feff8d37e61e2b', b'3de0236d0c3589e55861076bc4f42682', b'f3118e6239f1927afe424c96bc949191', b'bee0087887b35b2a6f97f023d4de3119', b'586453459391b76828c9539ea4b2966f', b'3e6e2cb2839aca7b7ecdff35c8762caa', b'b1f3a511cafd8e17d30d3b2b12118bfb', b'29bf30ac4ade8a44615a1191f1fcd9e9', b'4f27d7c7ff1cd090e9fa3e6a72f1009e', b'ad84fcd9786f90d4f5936658b6d5204d', b'6ecf9ee8fd2d89401b177c7e063904a2', b'49f1fb5a5d504202bb5df69a61c90f0b', b'aa7218ea169cb5851d1e474dcc2834e6', b'd7476e29bdbc47833aec900f8649070a', b'025bc6a7826c0c96224b82ccf8d2678e', b'65a4f58971665abfb5e7a682402726dc', b'52ec2347aa8f34eacadc504c14a6eea8', b'9440531fd984534e12e0d84056974aac', b'547e444e9724315c70f863887968d857', b'197c2af7d3f4d986847e2106a29a9181', b'fae3b6af2aac89e5bd9bb3070ba2a54b', b'05512ccdf2ddae48585b814bdcd43098', b'b9e4cadbdbc88d57af129d49e55f96e6', b'af18bad97183c2cdc173e8d7319fab30', b'ec28245fda1319e5d565f6860ca5d267', b'89e5bc87b6a15a85862207c9cc872d7c', b'1b5171538d8482fee85559b48ed6f83d', b'1f65ee054fb6e8119c0facc59647e83d', b'45ebfdc63f2f347debad9ff57b8893d8', b'83c08615ef906386a47b622afac73d9d', b'16fd7ce3b707124c4694fe7a0a4ed4fb', b'6443b92059eb8e61922232bb39e12b5d', b'6cd44be579962d66c0094399dc4ed270', b'70e6b941f12aa36e31c63fff9bacf62c', b'38e8fbc1400819cc24e38cc21b84ccc4', b'48c2664a5866092df0bf42d734a246ca', b'fc7bed7c0006e9fe74241237ea8e2631', b'df04663f92ec3a82beec899d1add0641', b'86dcdc2f35e162c3d54c6e84e4877653', b'af9af0f0ecfb4c2b3b8ad8ec6e837b5d', b'b6ca2e83212ec9e8b5cfd4b72b00183e', b'cac5f24e15549bc126be0a969d222e00', b'4278b23104fc1350e753832a10e7216e', b'12c09c2fd89a91d85f202c9fda67ab03', b'c37f91c6a2205fa3a4a2dcb167844a97', b'6c8be5b9c96e07b00a9a45d0175c00d2', b'855d2e5e397810a2f93b78f88cb45ea3', b'f626b4d94c1dae51fdcf077806146927', b'99a8d5c2e33cb06ce3ff920ac1215e88', b'b83d003baa2f07300a2e44af383d8794', b'37347e706524035563bfba47b493d948', b'f157cbf93171a6f88c539c3d3d32b69f', b'fdd823b33069154f1ab524c187d8d6b8', b'986d95f5865958cd81581d3f6bfbd12d', b'99e4d2f30148e6a5c719a4e86881a639', b'049a89b17e328d6e99f0ed0abf80e520', b'018872866d7f6d87722b33de9d13c067', b'fd98bc8a385d8643b7e2c56d51e82d3b', b'c8d91edfce86f69ad5ac61896d1ee1e1', b'37b5ea9cbd360c7ebf3505cdd1e841fe', b'40f52c4bf02a25bf8e18f971a27b1346', b'5dd56d80dbc0c514bb49fc756c51b4f7', b'087e40e6b3c9d017a4b161e1b55fc290', b'fe9e8afe390919e040039f98160f9d83', b'dfc21956a73dcd6695ca69b7208c5a63', b'fce903722123fca3d433546448407376', b'4ce7af2a502fd19a9bc42f3ee1f9228d', b'037ae09e2f089763846468dec79d2649', b'b30b1e39a006e3201e8899bee0c0f488', b'500d60eb05b9e310a517630f6783eee3', b'1dacc155a8cd206751b554c74b50e65d', b'216daacf380e7ac5768db80b14df6240', b'3c5ac109972c62520bb9c50f3ad4f15e', b'5488d09b0c5b28240af7613ed849e677', b'48a3314e9de39c1bc4907c8fbf92f925', b'78d36ed48609f8b8009becb699f13dd7', b'7121326152d01260126712e453759b43', b'e7c620317edfc11e02ac3a914b9ecde3', b'f78201816eb567c077abb2f5245f3e2d', b'8b8c76d175aebba4c7790680d9bd0fe5', b'220b8655cdbddb67b8c4c61b7efe9cd8', b'1ffaaf6104bccb6dbc726652a282b635', b'973dc3dd0cd85e6b02c445e6edcf5154', b'6c575f31305f84b734b85412d2a8856e', b'f5c3aaad1da3c37580edf3f8a7332d36', b'23c40f8902c5b29fc6d9ac59afd8208d', b'e83c68668c3e4d367dd74c1d92cdd109', b'3c97520568aaeba55fda1023c57470b0', b'7bc4aa48ac3c07a3b999d2ece5d34406', b'd447e20e8ab3137b1148963d5e61e19a', b'cbd8dc4e643ac4644ea130048478cf7f', b'080948e0aa52ed92e6bafcdf06eee3b5', b'd76e34a7b9191813ee4793fb9d13a199', b'd8393ea4aefba82e2bc551f30fe75ddc', b'e1f4e4fed4f1122df0bb1a65e78dc924', b'cae8d41fc04de30e2b337056dbb3b2ab']

key = Square_attack(cts).Reverse_key()

print(key)
print(hexlify(key))