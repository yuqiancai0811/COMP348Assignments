(ns db
  (:require [clojure.string :as str]))

(defn parse-line [line]
  "Parses a single line of city data into a map."
  (let [parts (str/split line #"\|")]
    {:city (nth parts 0)
     :province (nth parts 1)
     :size (nth parts 2)
     :population (read-string (nth parts 3))
     :area (read-string (nth parts 4))}))

(defn load-data [filename]
  "Loads city data from a file, returns a vector of maps."
  (->> (slurp filename)
       (str/split-lines)
       (map parse-line)))

(def cities-db (load-data "cities.txt"))

; utility function: get city info
(defn city-info [city-name]
  "Returns the information of a specific city."
  (first (filter #(= (:city %) city-name) cities-db)))

