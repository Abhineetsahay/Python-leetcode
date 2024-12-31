import requests
import json


def fetchUser(username):
    url = f"https://alfa-leetcode-api.onrender.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        jsonData = response.json()
        outputFile = 'userData.json'
        with open(outputFile, 'w') as json_File:
            json.dump(jsonData, json_File, indent=4)
        print(f"User data saved to {outputFile}")
    else:
        print(f"Error fetching user data. Status code: {response.status_code}")


def fetchAcceptedSubmission(username):
    try:
        submission = int(input("Enter the number of successfull submissions to fetch(last 20 submissions ): "))
        url = f"https://alfa-leetcode-api.onrender.com/{username}/acSubmission?limit={submission}"
        response = requests.get(url)
        if response.status_code == 200:
            submissionData = response.json()
            outputFile = 'successfullSubmission.json'
            with open(outputFile, 'w') as json_File:
                json.dump(submissionData, json_File, indent=4)
            print(f"User data saved to {outputFile}")
        else:
            print(f"Error fetching submissions. Status code: {response.status_code}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("First, tell us about yourself...")
    username = input("Enter your LeetCode profile username: ")
    
    while True:
        print("\nAvailable options:")
        print("1. User Details")
        print("2. Accepted Submissions")
        print("3. Exit")
        
        try:
            userChoice = int(input("Enter your choice (1/2/3): "))
            if userChoice == 1:
                fetchUser(username)
            elif userChoice == 2:
                fetchAcceptedSubmission(username)
            elif userChoice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
