array_map(($x) ⇒ $x + 1, [1, 2, 3]);

~~~

array_map(function ($x) {
    return $x+1;
}, [1, 2, 3]);

---

$z = 1;

array_map(($x) ⇒ $x + $z, [1, 2, 3]);

~~~

$z = 1;

array_map(function ($x) use (&$z) {
    return $x+$z;
}, [1, 2, 3]);

---

array_map(($x) ⇒ ($x + 1), [1, 2, 3]);

~~~

array_map(function ($x) {
    return ($x+1);
}, [1, 2, 3]);

---

array_map(($x) ⇒ { return $x + 1; }, [1, 2, 3]);

~~~

array_map(function ($x) {
    return $x + 1;
}, [1, 2, 3]);

---

array_map($x ⇒ { return $x + 1; }, [1, 2, 3]);

~~~

array_map(function ($x) {
    return $x + 1;
}, [1, 2, 3]);

---

array_map($x ⇒ $x + 1, [1, 2, 3]);

~~~

array_map(function ($x) {
    return $x+1;
}, [1, 2, 3]);
