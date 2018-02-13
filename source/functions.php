<?php

Pre\Plugin\addFunction("shortClosersParser", function ($ast, $multiArgs = true) {
    if ($multiArgs) {
        $defined = [];

        foreach ($ast->{"·args"} as $node) {
            $defined[(string) $node["·arg"]["·argName"]] = true;
        }
    } else {
        $defined = [(string) $ast->{"·argName"} => true];
    }

    $scoped = [];
    $scope = new \Yay\Ast("·scope");

    foreach ($ast->{"* ·body"}->tokens() as $token) {
        if (
            $token->is(T_VARIABLE) &&
            ('$this' !== (string) $token) &&
            !isset($scoped[(string) $token]) &&
            !isset($defined[(string) $token])
        ) {
            $scope->push(new \Yay\Ast("·var", $token));
            $scoped[(string) $token] = true;
        }
    }

    $ast->append($scope);
});
