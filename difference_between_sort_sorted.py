# listにあるsort()メソッドとsorted()関数の違いreverse() メソッドと reversed() 関数も同様）
	# list.sort() メソッドはリストの中身を並び替えます。この時そのリスト自体を並び替えた状態にします。
	# sorted() 関数は並び替えた新しいリストを作成します。元のリストは影響を受けません。

lst1 = [1, 3, 2]
print("before sort()")
print("lst1 =", lst1)
lst1.sort()
print()
print("after sort()")
print("lst1 =", lst1)
print()
lst2 = [1, 3, 2]
lst2_sorted = sorted(lst2)
print("lst2_sorted =", lst2_sorted)
print("lst2 =", lst2)

# このようにメソッド（関数）を呼び出したことにより
# 状態が変わる（この場合 lst1 が並び替えられた）ようなメソッド（関数）を
# 副作用のあるメソッド（関数）、破壊的メソッド（関数）という呼びかたをします。
