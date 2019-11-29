
; Tail recursion

(define (replicate x n)
  (define (helper_replicate x n lst)
      (if (= n 0)
          lst
          (helper_replicate x (- n 1) (append lst (list x)) ) ) )
      (helper_replicate x n nil)

  )

(define (accumulate combiner start n term)
  (define (helper_accumulate n result)
      (if (= n 0)
          result
          (helper_accumulate (- n 1) (combiner result (term n)))))
      (helper_accumulate n start)
)

(define (accumulate-tail combiner start n term)
  (define (helper_accumulate n result)
      (if (= n 0)
          result
          (helper_accumulate (- n 1) (combiner result (term n)))))
      (helper_accumulate n start)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3
               (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)


(define (nondecreastream s)
    (if (null? s) nil (begin 
    (define (helper_within lst rest last)
        (if (null? rest) lst
        (if (>= (car rest) last)
            (helper_within (append lst (list (car rest))) (cdr-stream rest) (car rest))
            lst
        ))
    
    )
    (if (null? s) nil)
    (define result (helper_within (list (car s)) (cdr-stream s) (car s)))
 
    (define length (length result))
    
    (define (helper_stream lst n)
        (if (null? lst) nil
        (if (= n 0)
            lst
            (helper_stream (cdr-stream lst) (- n 1)))
        
        ))
    
    (define rest_of_list (helper_stream s length))
    (cons-stream result (nondecreastream rest_of_list))

    )))


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))