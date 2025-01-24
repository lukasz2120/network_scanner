# Scanner seci L2

Skrypt ARP Scanner służy do skanowania sieci i wyświetlania adresów IP oraz odpowiadających im adresów MAC urządzeń w sieci lokalnej. Wykorzystuje bibliotekę `scapy` do tworzenia zapytań ARP i analizowania odpowiedzi.

## Funkcje

1. **`get_args()`**:  
   Funkcja umożliwia przekazywanie argumentów do skryptu z wiersza poleceń. Oczekuje, że użytkownik poda adres IP (lub zakres adresów), który ma zostać przeskanowany.

2. **`scan(ip)`**:  
   Funkcja, która wysyła zapytania ARP do podanego adresu IP i zbiera odpowiedzi, identyfikując urządzenia w sieci (adresy IP i MAC).

3. **`display_result(result)`**:  
   Funkcja wyświetla wyniki skanowania w formie tabeli zawierającej adresy IP i odpowiadające im adresy MAC.

## Jak używać

1. **Zainstaluj zależności**  
   Aby uruchomić skrypt, musisz mieć zainstalowaną bibliotekę `scapy`. Możesz ją zainstalować za pomocą `pip`:
   ```bash
   pip install scapy
