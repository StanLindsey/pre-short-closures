$fn = ($x) :callable => { return () => { return $x; }; };

~~~

$fn = function ($x) :callable {
    return [$x = $x ?? null, "fn" => function () use (&$x) {
        return $x;
    }]["fn"];
};
