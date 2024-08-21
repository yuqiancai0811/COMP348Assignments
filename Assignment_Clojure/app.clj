(ns app
  (:require [menu]))

(defn -main []
  "Entry point for the application, initializes data and displays the menu."
  (menu/init-menu))

(-main)
