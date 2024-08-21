(ns menu
  (:require [db]
            [clojure.string :as str]))

;; Declare functions to resolve forward references
(declare show-menu handle-choice list-cities-menu)

(defn list-all-cities []
  "Lists all cities ordered by city name."
  (println "[" (str/join " " (map #(str "\"" (:city %) "\"") (sort-by :city db/cities-db))) "]"))

(def size-map {"Large urban" 3, "Medium" 2, "Small" 1})

(defn list-cities-by-province []
  "Lists all cities for a given province ordered by size (descending) and name (ascending)."
  (println "Enter province name:")
  (let [province (str/trim (read-line))
        cities (->> (filter #(= (:province %) province) db/cities-db)
                    (sort-by #(vector (- (get size-map (:size %) 0)) (:city %))))]
    (doseq [city cities]
      (println (str "\"" (:city city) "\" \"" (:size city) "\" " (:population city))))))


(defn list-cities-by-density []
  "Lists all cities for a given province ordered by population density."
  (println "Enter province name:")
  (let [province (str/trim (read-line))
        density-fn (fn [city] (/ (:population city) (:area city)))
        cities (sort-by density-fn 
                        (filter #(= (:province %) province) db/cities-db))]
    (doseq [city cities]
      (println (str (str/join " " [(str "\"" (:city city) "\"") (:population city) (:area city)]))))))

(defn display-city-info []
  "Displays information for a given city."
  (println "Enter city name:")
  (let [city-name (str/trim (read-line))
        city (db/city-info city-name)]
    (if city
      (println city)
      (println "City not found."))))

(defn list-provinces []
  "Lists all provinces with the total number of cities."
  (let [province-counts (frequencies (map :province db/cities-db))
        sorted-provinces (sort-by second > province-counts)
        total-cities (reduce + (vals province-counts))]
    (doseq [[province count] sorted-provinces]
      (println (str "[" province " " count "]")))
    (println (str "Total: " (count sorted-provinces) " provinces, " total-cities " cities on file."))))
    
(defn display-province-info []
  "Displays total population for each province sorted by name."
  (let [province-pops (map (fn [province]
                             [province (reduce + (map :population (filter #(= (:province %) province) db/cities-db)))])
                           (distinct (map :province db/cities-db)))]
    (doseq [province (sort-by first province-pops)]
      (println (str "[" (first province) "] " (second province))))))

      
(defn list-cities-menu []
  "Sub-menu for listing cities."
  (println "1. List all cities\n"
           "2. List cities by province\n"
           "3. List cities by population density\n"
           "Enter an option or 'return' to go back:")
  (let [choice (read-line)]
    (cond
      (= choice "1") (do (list-all-cities) (list-cities-menu))
      (= choice "2") (do (list-cities-by-province) (list-cities-menu))
      (= choice "3") (do (list-cities-by-density) (list-cities-menu))
      (= choice "return") (show-menu)
      :else (do (println "Invalid option, please try again.") (list-cities-menu)))))

(defn show-menu []
  "Displays the main menu and handles user input."
  (println "*** City Information Menu ***\n"
           "1. List Cities\n"
           "2. Display City Information\n"
           "3. List Provinces\n"
           "4. Display Province Information\n"
           "5. Exit\n"
           "Enter an option?")
  (flush)
  (handle-choice))

(defn handle-choice []
  "Processes the user's menu choice."
  (let [choice (read-line)]
    (case choice
      "1" (list-cities-menu)
      "2" (do (display-city-info) (show-menu))
      "3" (do (list-provinces) (show-menu))
      "4" (do (display-province-info) (show-menu))
      "5" (println "Good Bye")
      (do (println "Invalid option, please try again.") (show-menu)))))

(defn init-menu []
  "Initializes the menu by loading data and displaying the main menu."
  (show-menu))

