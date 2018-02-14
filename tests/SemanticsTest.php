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

        $this->assertEvaluatedCodeEquals($code, 5);
    }

    private function assertEvaluatedCodeEquals($code, $expected)
    {
        $this->assertEquals($expected, eval(substr($code, strlen('<?php'))), $code);
    }

    /**
     * @test
     */
    public function can_process_single_expression_bodies()
    {
        Pre\Plugin\addMacro(__DIR__ . "/../source/macros.yay");

        $code = Pre\Plugin\parse('<?php
            $b = 2;
            return ($a ⇒ $a + $b)(3);
        ');

        $this->assertEvaluatedCodeEquals($code, 5);
    }
}
