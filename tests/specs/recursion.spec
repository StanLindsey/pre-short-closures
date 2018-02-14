$cb = () => {
    return () => {
        return () => {
            return "hello world";
        };
    };
};

~~~

$cb = function () {
    return function () {
        return function () {
            return "hello world";
        };
    };
};

---

$foo = "hello";
$bar = "world";

$cb = () => {
    return () => {
        return () => {
            print $foo . $bar;
        };
    };
};

~~~

$foo = "hello";
$bar = "world";

$cb = function () use (&$foo, &$bar) {
    return function () use (&$foo, &$bar) {
        return function () use (&$foo, &$bar) {
            print $foo . $bar;
        };
    };
};
