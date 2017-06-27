(define (find s predicate)
  'YOUR-CODE-HERE
  (cond
    ((null? s) #f)
    ((predicate (car s)) (car s))
    (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
  'YOUR-CODE-HERE
   (cond
     ((null? s) #t)
     ((find (cdr-stream s) (lambda (x) (= x (car s)))) #t)
     (else has-cycle (cdr-stream s))
   )
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
