window.onload = function() {
    document.getElementById('startAppButton').addEventListener('click', function() {
        // Tasks and advanced tasks arrays
        const tasks = []
        const advancedTasks = []
    
        // Prompt user for their name
        let name = prompt("Hello there, what's your name?")

        while (!name) {
            name = prompt("Hello there, what's your name?")
        }
    
        function main() {
            // Display menue options
            displayBasicOptions()
    
            // Prompt user for a pick
            const option = prompt(`Hi ${name}, please pick an option.`)
    
            if (option == 1) {
                addTask()
            } else if (option == 2) {
                deleteTask()
            } else if (option == 3) {
                listTasks()
                main()
            } else if (option == 4) {
                advanced()
            } else if (option == 5) {
                exit()
            } else {
                // Validate user input
                console.log("\nThat was invalid.")
                console.log("1. Continue")
                console.log("2. Exit")
    
                // Propmpt user if they want to continue
                const continueCheck = prompt(`Please choose carefully this time ${name}.`)
    
                // Check user input
                if (continueCheck == 1) {
                    main()
                } else {
                    exit()
                }
            }
        }
    
        function advanced() {
            // Display advanced menu options
            displayAdvancedOptions()
    
            // Prompt user for a pick
            const option = prompt(`${name} baceame a professional. Please pick an option.`)
    
            if (option == 1) {
                addTaskAdvanced()
            } else if (option == 2) {
                listTasksAdvanced()
                advanced()
            } else if (option == 3) {
                searchTask()
            } else if (option == 4) {
                modifyTask()
            } else if (option == 5) {
                clearTasks()
            } else if (option == 6) {
                main()
                return
            } else {
                // Validate user input
                console.log("\nThat was invalid.")
                console.log("1. Home")
                console.log("2. Advanced")
    
                // Propmpt user if they want to continue
                const continueCheck = prompt(`Please choose carefully this time ${name}.`)
    
                // Check user input
                if (continueCheck == 2) {
                    advanced()
                } else {
                    main()
                    return
                }
            }
        }
    
        function displayBasicOptions() {
            // Main menu
            console.log("\nbetterMe: Task Manager")
            console.log("1. Add task")
            console.log("2. Delete task")
            console.log("3. List tasks")
            console.log("4. Advanced")
            console.log("5. Exit")
        }
    
        function addTask() {
            // Prompt user for task input
            taskTitle = prompt("Task (m for main menu)")
    
            // Validate user task input
            if (taskTitle.trim() === "") {
                console.log("\nTask cannot be empty.")
            } else if (taskTitle === "M" || taskTitle === "m") {
                main()
                return
            } else {
                // Add to tasks array
                tasks.push(taskTitle)
    
                // Create advanced task
                const advancedTask = {
                    task: taskTitle,
                    group: null,
                    priority: null,
                    dueDate: null,
                    description: null,
                }
    
                // Add advanced task to array
                advancedTasks.push(advancedTask)
    
                console.log(`\nTask "${taskTitle}" has been added.`)
            }
    
            // Go back to main menu
            main()
            return
        }
    
        function deleteTask() {
            if (isEmpty()) {
                // Check if tasks array is empty
                console.log("\nThere are no tasks yet to delete.")
            } else {
                // Display tasks
                listTasks()
    
                // Prompt user for task index
                const deleteIndex = prompt("Please pick task index (m for main menu).")
    
                // Validate user input
                if (isNaN(deleteIndex) || deleteIndex < 1 || deleteIndex > tasks.length) {
                    console.log("\nInvalid task index.")
                } else if (deleteIndex === 'M' || deleteIndex === 'm') {
                    main()
                    return
                } else {
                    // Prompt user for confirmation
                    const deleteConfirmation = prompt("Are you sure you want to delete? Y or y for yes.")
    
                    if (deleteConfirmation === 'Y' || deleteConfirmation === 'y') {
                        // Delete task
                        console.log(`\nTask "${tasks[deleteIndex - 1]}" has been deleted.`)
                        tasks.splice(deleteIndex - 1, 1)
                        advancedTasks.splice(deleteIndex - 1, 1)
                    } else {
                        // Cancell the process
                        console.log("\nCancelled")
                    }
                }
            }
    
            // Go back to main menu
            main()
            return
        }
    
        function listTasks() {
            if (isEmpty()) {
                // Check tasks array isn't empty
                console.log("\nThere are no tasks yet.")
            } else {
                // Display tasks
                console.log('\nTasks:')
                tasks.forEach((task, index) => console.log(`${index + 1}. ${task}`))
            }
        }
    
        function exit() {
            // Display goodbye message
            console.log(`\nThanks ${name} for using betterMe. See you soon!`)
        }
    
        function displayAdvancedOptions() {
            // Advanced menu
            console.log("\nbetterMe: Task Manager (Advanced)")
            console.log("1. Add task (Advanced)")
            console.log("2. List tasks (Advanced)")
            console.log("3. Search task")
            console.log("4. Modify task")
            console.log("5. Clear tasks")
            console.log("6. Home")
        }
    
        function addTaskAdvanced() {
            // Create advanced task
            const advancedTask = {
                task: null,
                group: null,
                priority: null,
                dueDate: null,
                description: null,
            }
    
            // Prompt user for task input
            const taskTitle = prompt("Task (m for main menu): ")
    
            // Validate user task input
            if (taskTitle.trim() === "") {
                console.log("\nTask cannot be empty.")
                advanced()
                return
            } else if (taskTitle === "M" || taskTitle === "m") {
                advanced()
                return
            } else {
                // Add to tasks array
                tasks.push(taskTitle)
    
                // Update object task title
                advancedTask.task = taskTitle
            }
    
            // Prompt user for task group and update object
            const group = prompt("Group: ")
    
            // Check group input
            if (group) {
                advancedTask.group = group
            } else {
                console.log('\nNo group was added. You can add group later.')
            }
    
            // Display priorities and prompt user for it
            displayPriorities()
    
            // Prompt user for priority
            const priority = prompt("Priority (1-3): ")
    
            // Check user input
            if (priority == 1) {
                advancedTask.priority = "High"
            } else if (priority == 2) {
                advancedTask.priority = "Medium"
            } else if (priority == 3) {
                advancedTask.priority = "Low"
            } else {
                console.log('\nNo priority added. You can add priority later.')
            }
    
            // Prompt user fro due date
            const dueDate = prompt("Due date (DD-MM-YYYY): ")
    
            // Validate due date
            if (dueDate.trim() === "") {
                console.log('\nNo due date added. You can add due date later.')
            } else if (isValidDueDate(dueDate)) {
                advancedTask.dueDate = dueDate
            } else {
                console.log("\nInvalid due date. You can due date later")
            }
    
            // Prompt user for description
            const description = prompt("Description: ")
    
            // Check description input
            if (description) {
                advancedTask.description = description
            } else {
                console.log('\nNo description added. You can add description later.')
            }

            // Add advanced task to array
            advancedTasks.push(advancedTask)

            // Show that task has been added
            console.log(`\nTask "${taskTitle}" has been added.`)
    
            // Go to advanced menu
            advanced()
        }
    
        function listTasksAdvanced() {
            if (isEmpty()) {
                // Check tasks array isn't empty
                console.log("\nThere are no tasks yet.")
            } else {
                // Display tasks with all properties
                console.log('\nAdvanced Tasks:')
                advancedTasks.forEach((task, index) => console.log(`${index + 1}. Task: ${task.task}, Group: ${task.group}, Priority: ${task.priority}, Due Date: ${task.dueDate}, Description: ${task.description}`))
            }
        }
    
        function searchTask() {
            if (isEmpty()) {
                // Check tasks array isn't empty
                console.log("\nThere are no tasks yet to search.")
            } else {
                // Prompt user for keyword
                const keyword = prompt("Enter keyword")
    
                // Validate input
                if (keyword.trim() === "") {
                    console.log("\nKeyword cannot be empty.")
                    advanced()
                    return
                } else {
                    console.log("\n")
                    advancedTasks.forEach((object, index) => {
                        // Check if any task includes the keyword
                        if (object.task.includes(keyword)) {
                            // Add object to found array
                            tasksFound = true
                            console.log(`${index + 1}. ${object.task}`)
                        }
                    })
                }
    
                // Display search output
                if (!tasksFound) {
                    console.log(`\nNo tasks found that contain the keyword ${keyword}`)
                }
            }
    
            // Go to advanced menu
            advanced()
        }
    
        function modifyTask() {
            if (isEmpty()) {
                // Check tasks array isn't empty
                console.log("\nThere are no tasks yet to modify.")
            } else {
                // Display tasks
                listTasksAdvanced()
    
                // Prompt user for task index
                const modifyIndex = prompt("Please pick task index (m for main menu).")
    
                // Validate user input
                if (isNaN(modifyIndex) || modifyIndex < 1 || modifyIndex > tasks.length) {
                    console.log("\nInvalid task index.")
                } else if (modifyIndex === 'M' || modifyIndex === 'm') {
                    advanced()
                } else {
                    // Display modify options
                    displayModifyOptions()
    
                    const option = prompt("Please pick what you want to modify.")
    
                    if (option == 1) {
                        // Change task title
                        const newTaskTitle = prompt("Please pick a new task title (m for main menu)")
    
                        // Validate input
                        if (newTaskTitle.trim() === "") {
                            console.log("\nTask cannot be empty.")
                        } else if (newTaskTitle === "M" || newTaskTitle === "m") {
                            advanced()
                            return
                        } else {
                            // Display that it's been updated
                            console.log(`\nTask "${tasks[modifyIndex - 1]}" has been changed to "${newTaskTitle}"`)
    
                            // Update task title
                            tasks[modifyIndex - 1] = newTaskTitle
                            advancedTasks[modifyIndex - 1].task = newTaskTitle
                        }
    
                    } else if (option == 2) {
                        // Change task group
                        const newGroup = prompt("Please pick a new task group (m for main menu)")
    
                        // Validate input
                        if (newGroup === "M" || newGroup === "m") {
                            advanced()
                            return
                        } else {
                            // Display that it's been updated
                            console.log(`\nTask group "${advancedTasks[modifyIndex - 1].group}" has been changed to "${newGroup}"`)
    
                            // Update task group
                            advancedTasks[modifyIndex - 1].group = newGroup
                        }
                    } else if (option == 3) {
                        // Display priorities
                        displayPriorities()
    
                        // Prompt user for priority
                        const newPriority = prompt("Please pick a new priority 1-3 (m for main menu)")
    
                        // Check user input
                        if (newPriority === "M" || newPriority === "m") {
                            advanced()
                            return
                        } else if (newPriority == 1) {
                            console.log(`\nTask priority "${advancedTasks[modifyIndex - 1].priority}" has been changed to "High"`)
                            advancedTasks[modifyIndex - 1].priority = "High"
                        } else if (newPriority == 2) {
                            console.log(`\nTask priority "${advancedTasks[modifyIndex - 1].priority}" has been changed to "Medium"`)
                            advancedTasks[modifyIndex - 1].priority = "Medium"
                        } else if (newPriority == 3) {
                            console.log(`\nTask priority "${advancedTasks[modifyIndex - 1].priority}" has been changed to "Low"`)
                            advancedTasks[modifyIndex - 1].priority = "Low"
                        } else {
                            console.log("\nInvalid input. Priority hasn't been modified.")
                        }
    
    
                    } else if (option == 4) {
                        // Prompt user for due date
                        const newDueDate = prompt("Please pick a new due date DD-MM-YYYY (m for main menu)")
    
                        // Check input
                        if (newDueDate === "M" || newDueDate === "m") {
                            advanced()
                            return
                        } else if (isValidDueDate(newDueDate)) {
                            // Display and update due date
                            console.log(`\nTask due date "${advancedTasks[modifyIndex - 1].dueDate}" has been changed to "${newDueDate}"`)
                            advancedTasks[modifyIndex - 1].dueDate = newDueDate
                        } else {
                            console.log("\nInvalid input. Due date hasn't been modified.")
                        }
                    } else if (option == 5) {
                        // Prompt user for description
                        const newDescription = prompt("Please pick a new description (m for main menu)")
    
                        // Check input
                        if (newDescription === "M" || newDescription === "m") {
                            advanced()
                            return
                        } else {
                            // Display that it's been updated
                            console.log(`\nDescription "${advancedTasks[modifyIndex - 1].description}" has been changed to "${newDescription}"`)
    
                            // Update task description
                            advancedTasks[modifyIndex - 1].description = newDescription
                        }
                    } else {
                        console.log("Invalid pick.")
                    }
                }
            }
    
            // Go to advanced menu
            advanced()
        }
    
        function clearTasks() {
            if (isEmpty()) {
                // Check if tasks array is empty
                console.log("\nTasks already empty.")
            } else {
                // Prompt user for confirmation
                const clearConfirmation = prompt(`${name}, are you sure you want to clear tasks? Y or y for yes.`)
        
                if (clearConfirmation === 'Y' || clearConfirmation === 'y') {
                    // Clear tasks
                    console.log(`\nTasks have been cleared.`)
                    tasks.length = 0
                    advancedTasks.length = 0
                } else {
                    // Cancell the process
                    console.log("\nCancelled")
                }
            }
    
            // Go back to advanced menu
            advanced()
        }
    
        function displayPriorities() {
            console.log("\n1. High")
            console.log("2. Medium")
            console.log("3. Low")
        }
    
        function displayModifyOptions() {
            console.log("\n1. Task")
            console.log("2. Group")
            console.log("3. Priority")
            console.log("4. Due date")
            console.log("5. Description")
        }
    
        function isValidDueDate(dateString) {
            // Regular expression to match the format DD-MM-YYYY
            const dateRegex = /^\d{2}-\d{2}-\d{4}$/
            // Check if the input matches the DD-MM-YYYY format
            if (!dateRegex.test(dateString)) {
                return false // If not, it's not valid
            }
        
            // Extract the day, month, and year from the input
            const [day, month, year] = dateString.split('-').map(Number)
        
            // Create a new Date object with the extracted values
            const date = new Date(year, month - 1, day)
        
            // Validate the date
            const isValid =
            date.getDate() === day &&
            date.getMonth() === month - 1 &&
            date.getFullYear() === year
        
            if (!isValid) {
                return false // If the date isn't valid, return false
            }
        
            // Get today's date, setting time to the start of the day for comparison
            const today = new Date()
            today.setHours(0, 0, 0, 0) // Reset time to midnight to avoid time-related issues
        
            // Check if the provided date is prior to today
            if (date < today) {
                return false // If it's earlier than today, return false
            }
        
            return true // The date is valid and not in the past
        }
    
        function isEmpty() {
            // Check if tasks array is empty
            return tasks.length === 0
        }
    
        main()
    });
}
