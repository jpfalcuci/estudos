package AulaAnnotation;

@interface AnnotationInformacao {
	String autor();
	int    aulaEADNumero();
	String website() default "https://www.proway.com.br";
}
