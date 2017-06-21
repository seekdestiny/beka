(define (how-many-dots s)
  'YOUR-CODE-HERE
  (if (not (pair? s)) 0
    (+ (if (number? (cdr s)) 1 0)
       (how-many-dots (car s))
       (how-many-dots (cdr s)))
  )
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7)))))))
; expect 0
