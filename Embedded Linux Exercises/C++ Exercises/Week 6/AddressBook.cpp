/**
 *===================================================================================
 * @file           : AddressBook.cpp
 * @author         : Ali Mamdouh
 * @brief          : Impelementation of cAddress book to add contacts
 * @Version        : 1.0.0
 *===================================================================================
 * 
 *===================================================================================
 */
 
 


/*============================================================================
 ******************************  Includes  ***********************************
 ============================================================================*/ 
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>



/*============================================================================
 ****************************  Type Definitions  *****************************
 ============================================================================*/

/**
 * A structure representing a contact with a name and phone number.
 */
struct Contact 
{
    std::string name;  ///< Name of the contact.
    std::string phone; ///< Phone number of the contact.
};






/**
 * The AddressBook class manages a collection of contacts, providing functions
 * for adding, updating, deleting, searching, and listing contacts.
 */
class AddressBook 
{
private:
    std::vector<Contact> contacts; ///< List of contacts in the address book.

    /**
     * Sets the name for a contact by prompting the user.
     *
     * @param WantedContact: The contact whose name will be set.
     */
    void NameSetter(Contact& WantedContact);

    /**
     * Sets the phone number for a contact by prompting the user.
     *
     * @param WantedContact: The contact whose phone number will be set.
     */
    void PhoneSetter(Contact& WantedContact);

    /**
     * Retrieves the name of a given contact.
     *
     * @param WantedContact: The contact whose name will be retrieved.
     * @return The name of the contact.
     */
    std::string Namegetter(const Contact& WantedContact) const;

    /**
     * Retrieves the phone number of a given contact.
     *
     * @param WantedContact: The contact whose phone number will be retrieved.
     * @return The phone number of the contact.
     */
    std::string Phonegetter(const Contact& WantedContact) const;

    /**
     * Prompts the user to add a new contact to the address book.
     */
    void AddContact();

    /**
     * Prompts the user to update an existing contact's name, phone number, or both.
     */
    void UpdateContact();

    /**
     * Searches for a contact by name and displays the contact if found.
     */
    void SearchContact();

    /**
     * Displays the menu of available options for managing contacts.
     */
    void displayMenu() const;

    /**
     * Lists all contacts in the address book.
     */
    void ListContacts() const;

    /**
     * Prompts the user to delete a contact by selecting it from the list.
     */
    void DeleteContact();

    /**
     * Deletes all contacts in the address book.
     */
    void DeleteAllContacts();

    /**
     * Gets a valid choice from the user within the specified range.
     *
     * @param min: The minimum valid choice.
     * @param max: The maximum valid choice.
     * @return A valid choice within the specified range.
     */
    int getValidChoice(int min, int max) const;

    /**
     * Gets a valid index for selecting a contact from the list.
     *
     * @return A valid index for the contact list.
     */
    size_t getValidIndex() const;

public:
    /**
     * Runs the address book application, displaying the menu and processing user input.
     */
    void run();
};




/*============================================================================
 ****************************  Impelementations  *****************************
 ============================================================================*/

/**
 * Prompts the user to enter a name for the given contact.
 * Ensures the name is not empty.
 *
 * @param WantedContact: The contact whose name is being set.
 */
void AddressBook::NameSetter(Contact& WantedContact) 
{
    do 
    {
        std::cout << "Enter name: ";
        std::getline(std::cin >> std::ws, WantedContact.name);
    } while (WantedContact.name.empty());
}








/**
 * Prompts the user to enter a phone number for the given contact.
 * Ensures the phone number is not empty.
 *
 * @param WantedContact: The contact whose phone number is being set.
 */
void AddressBook::PhoneSetter(Contact& WantedContact) 
{
    do 
    {
        std::cout << "Enter phone: ";
        std::getline(std::cin >> std::ws, WantedContact.phone);
    } while (WantedContact.phone.empty());
}








/**
 * Adds a new contact to the address book by prompting the user for name and phone number.
 * The contact is then added to the contact list.
 */
void AddressBook::AddContact() 
{
    Contact newContact;
    NameSetter(newContact);
    PhoneSetter(newContact);
    contacts.push_back(newContact);
    std::cout << "Contact added successfully.\n";
}








/**
 * Retrieves the name of the specified contact.
 *
 * @param WantedContact: The contact whose name is to be retrieved.
 * @return The name of the contact.
 */
std::string AddressBook::Namegetter(const Contact& WantedContact) const 
{
    return WantedContact.name;
}








/**
 * Retrieves the phone number of the specified contact.
 *
 * @param WantedContact: The contact whose phone number is to be retrieved.
 * @return The phone number of the contact.
 */
std::string AddressBook::Phonegetter(const Contact& WantedContact) const 
{
    return WantedContact.phone;
}








/**
 * Lists all contacts in the address book, displaying their names and phone numbers.
 * If no contacts are found, a message is displayed indicating the list is empty.
 */
void AddressBook::ListContacts() const 
{
    if (contacts.empty()) 
    {
        std::cout << "No contacts found.\n";
        return;
    }

    for (size_t i = 0; i < contacts.size(); ++i) 
    {
        std::cout << i + 1 << ". Name: " << Namegetter(contacts[i])
                  << ", Phone: " << Phonegetter(contacts[i]) << "\n";
    }
}








/**
 * Allows the user to update an existing contact by searching for it by name or phone number.
 * The user can choose to update the name, phone number, or both.
 */
void AddressBook::UpdateContact() 
{
    if (contacts.empty()) 
    {
        std::cout << "No contacts to update.\n";
        return;
    }

    ListContacts();
    
    std::string search_term;
    std::cout << "Enter the name or phone number of the contact to update: ";
    std::getline(std::cin >> std::ws, search_term);

    auto it = std::find_if(contacts.begin(), contacts.end(),
                           [&](const Contact& c) { 
                               return c.name == search_term || c.phone == search_term; 
                           });

    if (it == contacts.end()) 
    {
        std::cout << "Contact not found.\n";
        return;
    }

    std::cout << "Contact found: Name: " << it->name << ", Phone: " << it->phone << "\n";
    
    std::cout << "1 - Change name\n2 - Change phone number\n3 - Change both\n";
    int option = getValidChoice(1, 3);
    
    switch (option) 
    {
        case 1:
            NameSetter(*it);
            break;
        case 2:
            PhoneSetter(*it);
            break;
        case 3:
            NameSetter(*it);
            PhoneSetter(*it);
            break;
    }
    std::cout << "Contact updated successfully.\n";
}








/**
 * Prompts the user to delete a contact from the address book by selecting it from the list.
 * The selected contact is then removed from the contact list.
 */
void AddressBook::DeleteContact() 
{
    if (contacts.empty()) 
    {
        std::cout << "No contacts to delete.\n";
        return;
    }

    ListContacts();
    size_t index = getValidIndex();
    contacts.erase(contacts.begin() + index);
    std::cout << "Contact deleted successfully.\n";
}







/**
 * Searches for a contact in the address book by name.
 * If the contact is found, its details are displayed; otherwise, a message is shown.
 */
void AddressBook::SearchContact() 
{
    if (contacts.empty()) 
    {
        std::cout << "No contacts to search.\n";
        return;
    }

    std::string name;
    std::cout << "Enter the name to search: ";
    std::getline(std::cin >> std::ws, name);

    auto it = std::find_if(contacts.begin(), contacts.end(),
                           [&](const Contact& c) { return Namegetter(c) == name; });

    if (it != contacts.end()) 
    {
        std::cout << "Name: " << it->name << ", Phone: " << it->phone << "\n";
    } else 
    {
        std::cout << "Contact not found.\n";
    }
}








/**
 * Deletes all contacts from the address book.
 * After this operation, the contact list will be empty.
 */
void AddressBook::DeleteAllContacts() 
{
    contacts.clear();
    std::cout << "All contacts have been deleted.\n";
}







/**
 * Displays the menu of options for managing contacts in the address book.
 */
void AddressBook::displayMenu() const 
{
    std::cout << "\nWelcome to your favorite address book!\n"
              << "What do you want to do?\n"
              << "1. List        | Lists all users\n"
              << "2. Add         | Adds a user\n"
              << "3. Delete      | Deletes a user\n"
              << "4. Delete all  | Removes all users\n"
              << "5. Search      | Search for a user\n"
              << "6. Update      | Update a user\n"
              << "7. Close       | Closes the address book\n";
}








/**
 * Prompts the user to select a valid option from the menu, within the specified range.
 *
 * @param min: The minimum valid option.
 * @param max: The maximum valid option.
 * @return The valid option selected by the user.
 */
int AddressBook::getValidChoice(int min, int max) const 
{
    int choice;
    while (true) 
    {
        std::cout << "Enter your choice (" << min << "-" << max << "): ";
        std::cin >> choice;
        if (std::cin.fail() || choice < min || choice > max) 
        {
            std::cin.clear(); // Clear error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            std::cout << "Invalid choice, please try again.\n";
        } else 
        {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard any extra input
            break;
        }
    }
    return choice;
}







/**
 * Prompts the user to select a valid index for a contact from the list.
 *
 * @return The valid index of the selected contact.
 */
size_t AddressBook::getValidIndex() const 
{
    size_t index;
    while (true) 
    {
        std::cout << "Enter the index of the contact: ";
        std::cin >> index;
        if (std::cin.fail() || index < 1 || index > contacts.size()) 
        {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid index, please try again.\n";
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            break;
        }
    }
    return index - 1;
}







/**
 * Runs the address book application, displaying the menu and processing user input
 * until the user chooses to close the application.
 */
void AddressBook::run() 
{
    bool exit = false;
    while (!exit) 
    {
        displayMenu();
        int choice = getValidChoice(1, 7);
        switch (choice) 
        {
            case 1:
                ListContacts();
                break;
            case 2:
                AddContact();
                break;
            case 3:
                DeleteContact();
                break;
            case 4:
                DeleteAllContacts();
                break;
            case 5:
                SearchContact();
                break;
            case 6:
                UpdateContact();
                break;
            case 7:
                exit = true;
                std::cout << "Exiting the address book. Goodbye!\n";
                break;
        }
    }
}




/*============================================================================
 ******************************  Main Code  **********************************
 ============================================================================*/

/**
 * The main function to start the AddressBook application.
 * Creates an AddressBook object and runs the application.
 *
 * @return 0 on successful execution.
 */
int main() 
{
    AddressBook addressBook;
    addressBook.run();
    return 0;
}
