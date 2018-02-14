class Fixture
{
    public function foo($end, $thing)
    {
        return ($name) => {
            $this->something();
            return "hello {$name}{$end}{$thing}";
        };
    }
}

~~~

class Fixture
{
    public function foo($end, $thing)
    {
        return function ($name) use (&$end, &$thing) {
            $this->something();
            return "hello {$name}{$end}{$thing}";
        };
    }
}
