$fn = ($x) :callable => { return () => { return $x; }; };

~~~

$fn = function ($x) :callable {
    return function () use (&$x) {
        return $x;
    };
};
