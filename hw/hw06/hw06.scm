;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond ((> x 0) 1)
        ((= x 0) 0)
        (else -1)
  )
)

(define (square x) (* x x))

(define (pow b n)
    (cond ((= n 0) 1)
          ((even? n) (* (square b) (pow b (- n 2))))
          ((odd? n) (* b (square b) (pow b (- n 3))))
          )
)

(define (unique s)
  (if (null? s)
      nil
      (cons (car s) (unique (filter (lambda (x) (not (equal? (car s) x))) (cdr s))))
  )
)