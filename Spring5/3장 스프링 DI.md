### 1. 의존이란?

A 클래스가 어떤 처리를 위해 B 클래스의 메소드를 실행하는 경우, 이를 '의존'한다고 표현한다. 
즉, 변경에 따른 영향이 전파되는 관계를 의미한다.

- 의존 하는 대상을 구하는 방법
1) 클래스 내부에서 의존 하는 객체를 직접 생성 → 유지보수에서 문제 유발
2) **DI → 주인공! 스프링과 연관**
3) 서비스 로케이터


### 2. DI를 통한 의존 처리

"의존 객체를 직접 생성하지 말고, 전달받자."

객체를 만들어서 생성자로 주입하든 어떻게든 주입(전달)해줘야한다. 조금 복잡하지. 굳이 왜 이렇게 하나?

변경의 유연함이라는 강점때문에!


### 3. DI와 의존 객체 변경의 유연함

1) 객체 직접 생성하는 경우
```java
AService { Dao dao = new Dao(); }
BService { Dao dao = new Dao(); }
ChildDao extends Dao { ... }
```
여기서 ChildDao 의 기능을 쓰려면 AService, BService의 코드를 다 바꿔야해!

2) 의존성을 주입하는경우
```java
Dao dao = new Dao(); // → new ChildDao();
AService a = new AService(dao);
BSerivce b = new BService(dao);
```

수정할 코드가 한 곳으로 집중된다~!

### 4. 의존 주입 방법

1) 생성자 주입
2) setter 메소드 사용
3) 자동 주입 : `@Autowired`


### 5. 객체 조립기

: 의존 객체를 주입하여 서로 다른 두 객체를 조립하는 역할을 하는 Class
*객체들을 생성*해서 *서로서로 주입해주는 클래스*가 따로 있으면 편하지 않을까? → 조립기 등장!


### 6. 스프링의 DI 설정

스프링이 DI를 지원하는 조립기이다.
스프링이 어떤 객체를 생성하고, 어떻게 의존을 주입할지 정의한 설정 정보 클래스를 하나 두자.
그리고 `@Configuration` 어노테이션을 달아주자. '이거 보고 이대로 관계를 만들어줘. 조립해줘.'

```java
@Configuration
public class AppContext {
	@Bean
	public Dao dao() { // "dao"라는 이름이고 Dao 타입인 싱글톤 빈 객체 생성해 리턴
		return new Dao();
	}
	
	@Bean
	public Service service(Dao dao){
		return new Service(dao);
	}
}
```

메소드 이름을 빈 객체의 이름으로 사용하는 게 기본이다.

```java
// main.class
ApplicationContext context = new AnnotationConfigApplicationContext(AppContext.class);
```

이 설정 클래스를 쥐어주면서 스프링 컨테이너를 생성한다. 
이제 `context.getBean()` 같은 메소드를 쓸 수 있다. 



#### DI 방식 1) 생성자

```java
public class Service {
	private Dao dao;
	
	public Service(Dao dao) {
		this.dao = dao;
	}
	
	public Long regist(Request req) {
		Member m = dao.selectByEmail(req.getEmail()); // dao의 메소드 사용
		...
	}
}

@Configuration
public class AppContext {
	// 위 코드와 동일
}
```

빈 생성 시점에 모든 의존 객체가 주입된다.

객체를 사용할 때 이미 모든 객체가 주입되어 있는 완전한 상태이다.

#### DI 방식 2) setter

```java
public class InfoPrinter {
	private Dao dao;
	private Printer printer;
	
	public setDao(Dao dao) {
		this.dao = dao;
	}

	public setPrinter(Printer printer){
		this.printer = printer;
	}
}
```

```java
@Configuration
public class AppContext {
	@Bean
	public InfoPrinter infoPrinter(){
		InfoPrinter infoPrinter = new ();
		infoPrinter.setDao(dao());
		infoPrinter.setPrinter(printer());
		return infoPrinter;
	}
}
```

세터 메소드 이름을 통해 어떤 객체가 주입되는지 알 수 있다.
파라미터가 많을 때 쉽게 유추 가능하다.


### 7. @Configuration 설정 클래스의 @Bean 설정과 싱글톤

Dao가 여러 Service에 주입된다고 하자. 그럼 각 Service가 가지고 있는 Dao는 서로 다른 객체일까? 당연히 아니다. 스프링 컨테이너가 생성한 빈은 싱글톤 객체니까. `@Bean`이 붙은 메소드에 대해서는 한 개의 객체만 생성한다. 그리고 항상 같은 객체를 리턴한다.


### 8. 두 개 이상의 설정 파일 사용하기

스프링 컨테이너를 만들 때 설정 파일을 콤마로 구분해서 두 개 쥐어주면 된다.

```java
ApplicationContext context = new AnnotationConfigApplicationContext(1.class, 2.class);
```

```java
@Configuration
public class 1 {
	
	@Bean
	// Dao

	@Bean
	// Printer

}
```

```java
@Configuration
public class 2 {

	@Autowired private Dao dao;
	@Autowired private Printer printer;

	@Bean
	public Service service() {
		return new Service(dao);
	}
}
```

`@Autowired` 어노테이션은 스프링의 자동 주입 기능. 스프링은 해당 타입의 빈을 찾아서 필드에 할당한다. 


#### `@Import`

두 개 이상의 설정파일을 사용하는 또 다른 방법.

```java
// 단일 Import
@Configuration
@Import(AppConf2.class)
public class AppConf1 {
	...
}
```

```java
// 다중 Import
@Configuration
@Import({AppConf1.class, AppConf2.class})
public class AppConf3 {
	...
}
```

`AppConf2`도 함께 사용해서 컨테이너를 초기화하니, 컨테이너에게 `AppConf1`만 쥐어줘도 된다.
다중으로 `Import`하는 경우, 메인을 수정할 필요가 없다. 최상위 하나만 쥐어주면 되니까.


### 9. getBean() 사용법!

```java
Printer printer = context.getBean("BEAN NAME", BEANTYPE.class);
```

이름이 다르면 → `NoSuchBeanDefinitionException`

타입이 다르면 → `BeannotOfRequiredTypeException`

빈 타입이 하나뿐이면 이름은 생략해도 된다.

생략했는데 타입이 두 개면 → `NoUniqueBeanDefinitionException`



### 10. 주입 대상 객체를 모두 빈 객체로 설정해야하나?

Nope. 꼭 스프링 빈이 아니고, 일반 객체여도 주입할 수 있다.
다만, 스프링 컨테이너가 관리하지 않는 객체이니, `getBean()` 으로 구할 수도 없다.