<?php

use PHPUnit\Framework\TestCase;

class SemanticsTest extends TestCase
{
    /**
     * @test
     */
    public function can_bind_by_reference()
    {
        Pre\Plugin\addMacro(__DIR__ . "/../source/macros.yay");

        $code = Pre\Plugin\parse('<?php
            $b = 2;

            $cb = ($a) => {
                return $a + $b;
            };

            return $cb(3);
        ');
        
        $this->assertEquals(5, eval(substr($code, strlen('<?php'))), $code);
    }
}
