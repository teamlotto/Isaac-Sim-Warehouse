
(cl:in-package :asdf)

(defsystem "lotti_nav-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WhereIgo" :depends-on ("_package_WhereIgo"))
    (:file "_package_WhereIgo" :depends-on ("_package"))
  ))