```jsx
function foo() {
	x = 10;
}
foo();

console.log(x); // 10
```

foo 함수 내에서 선언하지 않은 x 변수에 값 10을 할당하면 x 변수를 찾아야 x에 값을 할당할 수 있기때문에 자바스크립트 엔진은 x 변수가 어디에서 선언되었는지 스코프 체인을 통해 검색함.

자바스크립트 엔진은 foo 함수의 스코프에서 x변수의 선언을 검색하고 없으면 x 변수를 검색하기 위해 foo 함수 컨텍스트의 상위 스코프(위 코드는 전역 스코프)에서 x 변수 선언을 검색

전역 스코프에도 x 변수의 선언이 없어서 `ReferenceError` 를 발생할 것 같지만 자바스크립트 엔진은 암묵적으로 전역 객체에 x 프로퍼티를 동적으로 생성하여 전역 객체의 x 프로퍼티는 마치 전역변수인 것처럼 사용할 수 있으며 이러한 현상을 **암묵적 전역**이라고 함.

하지만 이러한 암묵적 전역은 오류를 발생시킬 원인이 될 가능성이 크므로 개발자는 반드시 `var, let, const` 키워드를 사용해서 변수를 선언한 다음 사용해야 함

그러나 실수는 언제든지 발생할 수 있고 이를 지원하기 위해 ES5부터 `strict mode(엄격 모드)` 가 추가되었음. strict mode는 자바스크립트 언어의 문법을 좀 더 엄격하게 적용하여 오류를 발생시킬 가능성이 높거나, 자바스크립트 엔진의 최적화 작업에 문제를 일으킬 수 잇는 코드에 대해 명시적인 에러를 발생시킴.

ESLint 같은 린트 도구를 사용해도 strict mode와 유사한 효과를 얻을 수 있으며 린트 도구는 strict mode가 제한하는 오류는 물론 코딩 컨벤션을 설정 파일 형태로 정의하고 강제할 수 있기때문에 더욱 강력한 효과를 얻을 수 있어서 strict mode보다는 린트 도구의 사용을 선호하기도 함

`ESLint는 비주얼 스튜디오 코드에서 설치 및 사용 가능함`

## strict mode의 적용

strict mode를 적용하려면 전역의 선두 또는 함수 몸체의 선두에 `'use strict';` 를 추가함. 전역의 선두에 추가하면 스크립트 전체에 strict mode가 적용됨

```jsx
'use strict';

function foo() {
	x = 10; //ReferenceError: x is not defined
}
foo();
```

함수 몸체의 선두에 추가하면 해당 함수와 중첩 함수에 strict mode가 적용됨

```jsx
function foo() {
	'use strict';
	x = 10; //ReferenceError: x is not defined
}
foo();
```

코드의 선두에 ‘use strict’; 를 위치시키지 않으면 strict mode가 제대로 동작하지 않음

```jsx
function foo() {
	x = 10; //에러를 발생시키지 않음
	'use strict';
}
foo();
```

### 전역에 strict mode를 적용하는 것은 피할 것 !

전역에 적용한 strict mode는 스크립트 단위로 적용됨

```jsx
<!DOCTYPE html>
<html>
<body>
	<script>
		'use strict';
	</script>
	<script>
		x = 1; //에러가 발생하지 않음
		console.log(x); //1
	</script>
	<script>
		'use strict';
		y = 1; //ReferenceError: y is not defined
		console.log(y);
	</script>
</body>
</html>
```

위 코드와 같이 스크립트 단위로 적용된 strict mode는 다른 스크립트에 영향을 주지 않고 해당 스크립트에 한정되어 적용됨.

하지만 strict mode 스크립트와 non-strict mode 스크립트를 혼용하는 것은 오류를 발생 시킬 수 있고 외부 서드파티 라이브러리를 이용하는 경우 라이브러리가 non-strict mode인 경우도 있기때문에 전역에 strict mode를 적용하는것은 바람직하지 않음. 이러한 경우 즉시 실행 함수로 스크립트 전체를 감싸서 스코프를 구분하고 즉시 실행 함수의 선두에 strict mode를 적용함

```jsx
//즉시 실행 함수의 선두에 strict mode 적용
(function () {
	'use strict';
	//...
}());
```

### 함수 단위로 strict mode를 적용하는 것도 피할 것!

어떤 함수는 strict mode를 적용하고 어떤 함수는 strict mode를 적용하지 않는 것은 바람직하지 않으며 모든 함수에 일일이 strict mode를 적용하는 것은 번거로운 일임

```jsx
(function () {
	//non-strict mode
	var let = 10; //에러가 발생하지 않음
	 function foo() {
		'use strict';
		
		let = 20; //SyntaxError
		}
		foo();
}());
```

따라서 strict mode는 즉시 실행 함수로 감싼 스크립트 단위로 적용하는 것이 바람직함

## strict mode가 발생 시키는 에러

1. 암묵적 전역
    
    선언하지 않은 변수를 참조하면 `ReferenceError` 가 발생
    
    ```jsx
    (function () {
    	'use strict';
    	x = 1;
    	console.log(x); //ReferenceError : x is not defined
    }());
    ```
    
2. 변수, 함수, 매개변수의 삭제
    
    `delete` 연산자로 변수, 함수, 매개변수를 삭제하면 `SyntaxError` 가 발생
    
    ```jsx
    (function () {
    	'use strict';
    	
    	var x = 1;
    	delete x; //SyntaxError : Delete of an unqualified identifier in strict mode
    
    	function foo(a) {
    		delete a; //SyntaxError : Delete of an unqualified identifier in strict mode
    	}
    	delete foo; //SyntaxError : Delete of an unqualified identifier in strict mode
    }());
    ```
    
3. 매개변수 이름의 중복
    
    중복된 매개변수 이름을 사용하면 `SyntaxError` 가 발생
    
    ```jsx
    (function () {
    	'use strict';
    
    	//SyntaxError: Duplicate parameter name not allowed in this context
    	function foo(x, x){
    		return x+x;
    	}
    	console.log(foo(1,2));
    }());
    ```
    
4. with 문의 사용
    
    `with` 문을 사용하면 `SyntaxError` 가 발생함. with 문은 전달된 객체를 스코프 체인에 추가. `with` 문은 동일한 객체의 프로퍼티를 반복해서 사용할 때 객체 이름을 생략할 수 있어서 코드가 간단해지는 효과가 있지만 성능과 가독성이 나빠지는 문제가 있음. 따라서 `with` 문은 사용하지 않는 것이 좋음
    
    ```jsx
    (function (){
    	'use strict';
    	
    	//SyntaxError: Strict mode code may not include a with statement
    	with({ x:1 }){
    		console.log(x);
    	}
    }());
    ```
    

### strict mode 적용에 의한 변화

1. 일반함수의 this
    
    strict mode에서 함수를 일반 함수로서 호출하면 this에 `undefined` 가 바인딩 됨. 생성자 함수가 아닌 일반 함수 내부에서는 this를 사용할 필요가 없기 때문. 이때 에러는 발생하지 않음.
    
    ```jsx
    (function () {
    	'use strict';
    	
    	function foo() {
    		console.log(this); //undefined
    	}
    	foo();
    
    	function Foo(){
    		console.log(this); //Foo
    	}
    	new Foo();
    }());
    ```
    
2. arguments 객체
    
    strict mode에서는 매개변수에 전달된 인수를 재할당하여 변경해도 arguments 객체에 반영되지 않음
    
    ```jsx
    (function (a) {
    	'use strict';
    	//매개변수에 전달된 인수를 재할당하여 변경
    	a = 2;
    	
    	//변경된 인수가 arguments 객체에 반영되지 않음
    	console.log(arguments); // { 0 : 1, length: 1 }
    }(1));
    ```