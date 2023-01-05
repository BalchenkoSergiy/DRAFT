Main page Power Apps: (For running app)
    https://make.powerapps.com/environments/61be436c-10d7-e8dd-b075-1367221019f1/apps#

Link to my Pet project
    https://make.powerapps.com/e/61be436c-10d7-e8dd-b075-1367221019f1/s/82ecc8b3-a280-ed11-81ac-6045bd5cd155/app/edit/a6708dad-5081-ed11-81ac-6045bd5cd155

Create table
    Notes about tables:
        'Tables where formerly called entities'
        'A single row within a table is known as a record'
        'Tables have views, forms and business rules associated with them. Additionally, tables also have charts as well as dashboards where charts are presented.'
        'You can use standard tables, custom tables, or both'
        'You can’t delete standard tables, columns, or table relationships. They are considered part of the system solution and every organization is expected to have them.'
   
    Create table:
        1. '''New -> Table'''
        
        2. '''Введіть дані для наступних властивостей. (Enter data for the following properties):
            
            - Display name - Це єдина назва для таблиці, яка буде показана в додатку. Це можна змінити пізніше. 
                (This is the singular name for the table that will be shown in the app. This can be changed later.)
            
            - Plural display name - Це назва таблиці у множині, яка відображатиметься в програмі. Це можна змінити пізніше.
                (This is the plural name for the table that will be shown in the app. This can be changed later.)
            
            - Description - Змістовно опишіть призначення таблиці. (Provide a meaningful description of the purpose of the table.)
            
            - Enable Attachments - щоб додати нотатки та файли до записів цієї таблиці (to append notes and files to records for this table)
            
            - Advanced options - щоб відобразити додаткові властивості, необов’язкові для таблиці. 
                (to display additional properties that are optional for a table.)
                * Schema name - За замовчуванням ім’я схеми створюється автоматично на основі відображуваного імені, але ви можете змінити його. 
                    Ім’я схеми не може містити пробіли та містить префікс налаштування для видавця рішення Dataverse. 
                    Ви не можете змінити це після збереження таблиці.
                    (By default, the schema name is automatically created for you based on the display name, but you can change it. 
                    The schema name can't contain spaces and includes the customization prefix for the Dataverse solution publisher. 
                    You can't change this after the table is saved)
                
                * Type - Виберіть тип таблиці. Використовуйте стандарт для більшості таблиць. Таблиці активності — це спеціальна таблиця, 
                    яка може належати лише користувачу або команді, але не може належати організації. Віртуальні таблиці вимагають заповнення таблиці 
                    даними із зовнішнього джерела. (Select the type of table. Use standard for most tables. Activity tables are a special table that 
                    can only be owned by a user or team, but can’t be owned by an organization. Virtual tables require the table be populated with 
                    data from an external source.)
                
                * Record ownership - Тип права власності визначає, хто може виконувати операції над записом 
                    (The type of Ownership defines who can perform operations on a record)
                
                * Choose a table image - Це зображення відображається в Power Apps у деяких областях дизайну. Зверніть увагу, що зображення не 
                    відображається в програмах, які використовують таблицю. Щоб відображати зображення в програмах, використовуйте стовпець із зображеннями.
                    (This image is displayed in Power Apps in some design areas. Notice that the image doesn't appear in apps using the table. To display 
                    images in apps, use the image column.)
                
                * Color - Установіть колір, який використовуватиметься для таблиці в додатках, керованих моделлю 
                    (Set a color to be used for the table in model-driven apps)
                
                * Apply duplicate detection rules - ви зможете створити правила виявлення дублікатів для цієї таблиці 
                    (enabling this allows you to create duplicate detection rules for this table)
                
                * Track changes - Вмикає ефективну синхронізацію даних, виявляючи, які дані змінилися з моменту початкового вилучення або останньої 
                    синхронізації.
                    (Enables data synchronization in a performant way by detecting what data has changed since the data was initially extracted or last 
                    synchronized.)
                
                * Provide custom help - Якщо вибрано, установіть URL-адресу довідки , щоб контролювати, яку сторінку бачитимуть користувачі, коли натискатимуть 
                    кнопку довідки в програмі. Використовуйте це, щоб надати вказівки для процесів вашої компанії для таблиці.
                    (When selected, set a Help URL to control what page users will see when they select the help button in the application. Use this to provide 
                    guidance specific to your company processes for the table.)
                
                * Audit changes to its data - Якщо для вашої організації ввімкнено аудит, це дозволяє фіксувати зміни в записах таблиці з часом.
                    (When auditing is enabled for your organization, this allows for changes to table records to be captured over time.)
                
                * Leverage quick create form if available - Після того, як ви створите та опублікуєте форму швидкого створення для цієї таблиці, користувачі 
                    матимуть можливість створити новий запис за допомогою кнопки «Створити» на навігаційній панелі.
                    (After you've created and published a Quick Create Form for this table, people will have the option to create a new record using the 
                    Create button in the navigation pane.)
                    
                * Creating a new activity - Пов’яжіть дії із записами для цієї таблиці. (Associate activities to records for this table.)
                
                * Doing a mail merge - Користувачі програми можуть використовувати цю таблицю зі злиттям. (App users can use this table with mail merge.)
                
                * Setting up SharePoint document management - Після виконання інших завдань, щоб увімкнути керування документами для вашої організації, 
                    увімкнення цієї функції дозволить цій таблиці брати участь в інтеграції з SharePoint
                    (After other tasks have been performed to enable document management for your organization, enabling this feature allows for this 
                    table to participate in integration with SharePoint.)
                
                * Can have connections - Використовуйте функцію з’єднань, щоб показати, як записи для цієї таблиці мають з’єднання із записами інших таблиць, 
                    у яких також увімкнено з’єднання. (Use the connections feature to show how records for this table have connections to records of other 
                    tables that also have connections enabled.)
                
                * Can have a contact email - Надсилайте електронні листи, використовуючи адресу електронної пошти, збережену в одному з полів цієї таблиці. 
                    Якщо для цієї таблиці ще не існує стовпця з одним рядком тексту з форматом електронної пошти, новий стовпець буде створено, коли ви 
                    ввімкнете надсилання електронної пошти. (Send emails using an email address stored in one of the fields for this table. If a Single 
                    Line of Text column with format set to email doesn’t already exist for this table, a new one will be created when you enable sending email.)
                
                * Have an access team - Створіть командні шаблони для цієї таблиці. (Create team templates for this table.)
                
                * Can be linked to feedback - Дозвольте користувачам програми писати відгуки про будь-який запис таблиці або оцінювати записи таблиці в 
                    межах визначеного діапазону оцінок. 
                    (Let app users write feedback for any table record, or rate table records within a defined rating range.)
                
                * Appear in search results - щоб записи таблиці можна було включити в результати пошуку під час використання програми
                    (Enable so that table records can be included in search results when using an app.)
                
                * Can be taken offline - Робить дані в цій таблиці доступними, коли програма Power Apps не підключена до мережі.
                    (Makes data in this table available while the Power Apps application isn't connected to a network.)
                
                * Can be added to a queue - Черги покращують маршрутизацію та розподіл роботи, роблячи записи для цієї таблиці доступними в центральному місці, 
                    до якого кожен має доступ.
                    (Queues improve routing and sharing of work by making records for this table available in a central place that everyone can access)
                
            - Primary column - Виберіть вкладку « Основний стовпець », якщо потрібно змінити відображуване ім’я або назву основного стовпця
                (Select the Primary column tab if you want to change the Display Name or Name of the primary column)
            '''
        
    Edit Table:
        '''Під час перегляду таблиць виберіть таблицю, яку потрібно редагувати, а потім виберіть « Properties » на command bar, якщо ви хочете 
        редагувати властивості таблиці.  
        (While viewing tables, select the table you want to edit, and then select Properties from the command bar if you want to edit the table 
        properties.)'''
        
    Edit table components using the table hub:
        '''
        Щоб редагувати компоненти форми, відкрийте таблицю, щоб відобразити концентратор таблиці. Центр таблиці відображає компоненти таблиці, 
        описані в наступних розділах.
        (To edit form components, open the table to display the table hub. The table hub displays the table components described in the 
        following sections.)
        
            * Table properties - Відображає кілька загальних властивостей для таблиці. Виберіть «Properties» на панелі команд, щоб змінити 
                властивості таблиці. 
                (Displays a few common properties for the table. Select Properties on the command bar to edit the table properties.)
            
            * Schema - В області « Схема» виберіть із наведених нижче компонентів таблиці, щоб відкрити область, де можна переглянути 
                та відкрити існуючі компоненти або створити новий. 
                (From the Schema area select from the following table components to open the area where you can view and open existing 
                components or create a new one.):
                    * Columns. (Стовпці)            Link: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-fields
                    * Relationships. (Cтосунки)     Link: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships
                    * Keys. (Ключі)                 Link: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-alternate-keys-reference-records
            
            * Data experiences - виберіть із наведених нижче компонентів таблиці, щоб відкрити область, де можна переглянути та 
                відкрити наявні компоненти або створити новий. (select from the following table components to open the area where you 
                can view and open existing components or create a new one)
                    * Forms.                            Link: https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms
                    * Views.                            Link: https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views
                    * Charts. (Діаграми)                Link: https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-system-chart
                    * Dashboards. (Приладові панелі)    Link: https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-dashboards
            
            * Customizations - В області налаштувань виберіть із наведених нижче компонентів таблиці, щоб відкрити область, де можна 
                переглядати та відкривати наявні компоненти або створювати нові. (From the Customizations area select from the following table 
                components to open the area where you can view and open existing components or create a new one.)
                    * Business rules. (Правила ведення бізнесу) Link: https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-business-rules-recommendations-apply-logic-form
                    * Commands. (Команди)                       Link: https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/use-command-designer
            
            * Table columns and data - Перегляд і створення даних запису таблиці для таблиці (View and create table record data for the table.)
            
            * Table designer - У концентраторі таблиць виберіть « Редагувати », щоб відкрити конструктор таблиць. Конструктор таблиць 
                дозволяє вносити великі зміни в таблицю, включаючи редагування або додавання нових записів і стовпців, редагування 
                властивостей таблиці або створення програми на основі моделі на основі таблиці.
                (From the table hub, select Edit to open the table designer. The table designer lets you make extensive changes to a table 
                including editing or adding new records and columns, editing table properties, or creating a model-driven app based on the table.)
        '''
        
    Delete a table:
        '''Під час перегляду таблиць виберіть таблицю, а потім виберіть у меню Видалити .
        Якщо таблиця має залежності, які перешкоджають її видаленню, ви побачите повідомлення про помилку. 
        Щоб визначити та видалити будь-які залежності, вам знадобиться скористатися провідником рішень.
        (While viewing tables, select the table, and then select Delete from the menu.
        If the table has dependencies that prevent it from being deleted you'll see an error message. 
        To identify and remove any dependencies, you'll need to use the solution explorer.)
        '''
        
Create columns Different types, including calculated and rollup
    Наведена нижче таблиця містить відповідний AttributeTypeDisplayName тип API.
        (The following table includes the corresponding AttributeTypeDisplayName API type.)
        '''
            * Power Apps data type	* Solution Explorer type	                    * API type
            * Big Integer	        * Time Stamp	                                * BigIntType
            * Choice	            * Option Set	                                * PicklistType
            * Choices	            * MultiSelect Field	                            * MultiSelectPicklistType
            * Currency	            * Currency	                                    * MoneyType
            * Customer	            * Customer	                                    * CustomerType
            * Date and Time	        * Date and Time (Date and Time Format)          * DateTimeType
            * Date Only	            * Date and Time (Date Only Format)              * DateTimeType
            * Decimal Number	    * Decimal Number	                            * DecimalType
            * Duration	            * Whole Number (Duration Format)                * IntegerType
            * Email	                * Single Line of Text (Email Format)            * StringType
            * File	                * File	                                        * FileType
            * Floating Point Number	* Floating Point Number	                        * DoubleType
            * Image	                * Image	                                        * ImageType
            * Language	            * Whole Number (Language Format)                * IntegerType
            * Lookup	            * Lookup	                                    * LookupType
            * Multiline Text	    * Multiple Lines of Text	                    * MemoType
            * Owner	                * Owner	                                        * OwnerType
            * Phone	                * Single Line of Text (Phone Format)            * StringType
            * Status	            * Status	                                    * StateType
            * Status Reason	        * Status Reason	                                * StatusType
            * Text	                * Single Line of Text (Text Format)             * StringType
            * Text Area	            * Single Line of Text (Text Area Format)        * StringType
            * Ticker Symbol	        * Single Line of Text (Ticker Symbol Format)    * StringType
            * Timezone	            * Whole Number (Time Zone Format)               * IntegerType
            * Unique Identifier	    * Unique Identifier or Primary Key	            * UniqueidentifierType
            * URL	                * Single Line of Text (URL Format)              * StringType
            * Whole Number	        * Whole Number ( None Format)                   * IntegerType
            * Yes/No	            * Two Options	                                * BooleanType
        '''
    
    Типи стовпців, які використовує система. (Column types used by the system)
        Є деякі стовпці, що використовуються системою, які ви не можете додати за допомогою дизайнера.
        (There are some columns used by the system that you cannot add using the designer.)
        '''
            Type	                Description
            
            Time Stamp:	            Тип Big Integer, який використовується системою для запису номера версії для керування оновленнями таблиці.
                                    (A Big Integer type used by the system to capture a version number for managing updates to a table.)
            
            Customer:	            Стовпець пошуку, за допомогою якого можна вказати клієнта, який може бути обліковим записом або контактом.
                                    Примітка: Цей атрибут можна додати за допомогою конструктора дослідника рішень.
                                    (A lookup column that you can use to specify a customer, which can be an account or contact.
                                    Note: This attribute can be added using solution explorer designer.)
            
            Owner:	                Стовпець системного пошуку, який посилається на користувача або команду, якій призначено рядок таблиці, 
                                    що належить користувачу або команді.
                                    (A system lookup column that references the user or team that is assigned a user or team owned table row.)
            
            Status Reason:	        Системний стовпець із параметрами, які надають додаткові відомості про стовпець «Стан». Кожен параметр 
                                    пов’язаний з одним із доступних параметрів стану. Ви можете додавати та редагувати параметри.

                                    Ви також можете включити спеціальні переходи між станами, щоб контролювати, які параметри стану доступні 
                                    для певних таблиць.
                                    (A system column that has options that provide additional detail about the Status column. Each option 
                                    is associated with one of the available Status options. You can add and edit the options.
                    
                                    You can also include custom state transitions to control which status options are available for 
                                    certain tables. More information: Define status reason transitions for custom tables)
            
            Status:	                Системний стовпець із параметрами, які зазвичай відповідають активному та неактивному стану. 
                                    Деякі системні атрибути мають додаткові параметри, але всі настроювані атрибути мають лише параметри 
                                    статусу « Активний » і «Неактивний».
                                    (A system column that has options that generally correspond to active and inactive status. Some system 
                                    attributes have additional options, but all custom attributes have only Active and Inactive 
                                    status options.)
            
            Unique Identifier:	    Системний стовпець зберігає значення глобального унікального ідентифікатора (GUID) для кожного рядка.
                                    (A system column stores a globally unique identifier (GUID) value for each row.)
        '''
    

Create forms
    
        
Different types, including main, quick view and quick create
    Form types (Типи форм):
        - Main (the main user interface) (Головна (головний інтерфейс користувача))
            '''
                Used in model-driven apps, Dynamics 365 for tablets, and Dynamics 365 for Outlook
                These forms provide the main user interface for viewing and interacting with table data
                (Використовуються в пограмах на основі моделі, Dynamics 365 для планшетів і Dynamics 365 for Outlook
                Ці форми забезпечують основний інтерфейс користувача для перегляду даних таблиці та взаємодії з ними)
                https://learn.microsoft.com/uk-ua/power-apps/maker/model-driven-apps/media/main-form-dialog.gif
            '''
        - Quick create (rapid data entry) (Швидке створення (швидке введення даних))
            '''
                Used in model-driven apps, Dynamics 365 for tablets, and Dynamics 365 for Outlook.
                For updated tables, these forms provide a basic form optimized for creating new records.
                (Використовуються в пограмах на основі моделі, Dynamics 365 для планшетів і Dynamics 365 for Outlook.
                Для оновлених таблиць ці форми забезпечують базову форму, оптимізовану для створення нових записів.)
                https://learn.microsoft.com/uk-ua/power-apps/maker/model-driven-apps/media/quick-create-form.gif
            '''
        - Quick view (to see related data) (Швидке подання (для перегляду пов’язаних даних))
            '''
                Used in model-driven apps, Dynamics 365 for tablets, and Dynamics 365 for Outlook.
                For updated tables, these forms appear within the main form to display additional data for a row that is referenced 
                    by a lookup column in the form.
                Users can view data from related tables without having to leave the form.
                (Використовуються в пограмах на основі моделі, Dynamics 365 для планшетів і Dynamics 365 for Outlook.
                Для оновлених таблиць ці форми відображаються в основній формі для відображення додаткових даних для рядка, на який 
                    є посилання в стовпці підстановки у формі.
                Користувачі можуть переглядати дані з пов’язаних таблиць, не залишаючи форму.)
                https://learn.microsoft.com/uk-ua/power-apps/maker/model-driven-apps/media/quick-view-form-control.png
            '''
        - Card form (a compact view) (Форма картки (компактне подання))
            '''
                Used in views for model-driven apps. Card forms are designed to present information in a compact format that is 
                suitable for mobile devices.
                (Використовується в поданнях для модельних програм. Форми картки форми призначені для представлення відомостей у 
                компактному форматі, що підходить для мобільних пристроїв.)
                https://learn.microsoft.com/uk-ua/power-apps/maker/model-driven-apps/media/card-format.png
            '''

Create views
    '''Model-driven apps use views to define how a list of records for a specific table are displayed in the application (У модельних 
        програмах використовуються подання, за допомогою яких можна визначити, як список записів для певної таблиці відображається 
        у програмі.)'''
    Create a public view in Power Apps
    '''
        1. Sign in to Power Apps (Увійти до Power Apps)
        2. Select an environment (Виберіть середовище)
            It is best practice to create tables inside a custom solution. More information: Solution (glossary)
            (Краще створити таблиці в настроюваному рішенні. Додаткові відомості: Рішення (глосарій))
        3. Expand Data, select Tables, select the table you want, and then select the Views area. If using a custom solution, open 
            the solution, open the table, and then select the Views area.
            (Розгорніть Дані, виберіть Таблиці, виберіть потрібну таблицю, а потім виберіть область Подання. Якщо використовується 
            настроюване рішення, відкрийте рішення, відкрийте таблицю, а потім виберіть область Подання)
        4. On the toolbar, select Add view. (Виберіть Додати подання на панелі інструментів)
        5. On the Create a view dialog, enter a name and, optionally, a description, and then select Create. 
            (У діалоговому вікні Створити подання введіть ім'я і, за потреби, опис, а потім виберіть Створити)
        6. In the view designer, select + View column to add additional columns needed within the view. Or, select Table columns 
            in the left navigation and drag the table columns into your view.
            (У конструкторі подань виберіть + Стовпець подання, щоб додати стовпці, які ви бажаєте відображати в поданні. 
            Крім того, можна вибрати Стовпці таблиці в області переходів ліворуч і перетягнути стовпці таблиці в подання)
        7. In the view designer, the following tasks can be performed (У конструкторі подань можна виконати наступні завдання):
            - To change the column filtering select the header of the column where the filter is required, and then in the dropdown 
                list select Filter by. (Щоб змінити фільтрування стовпця, виберіть заголовок стовпця, який потрібно фільтрувати, 
                а тоді в розкривному списку виберіть Фільтрувати за)
            - To change the column sorting select the header of the column where sorting is needed then select Sort A-Z, Sort Z-A, 
                Sort descending, or Sort ascending. (Щоб змінити сортування стовпця, виберіть заголовок стовпця, в якому потрібно 
                сортувати дані, а потім виберіть Сортування А-Я, Сортування Я-А, Сортування за спаданням чи Сортування за зростанням)
            - Configure column width by selecting and dragging the column to the desired position.
            - Reorder columns by dragging a column to the desired position  (Настроювання ширини стовпця шляхом вибору та 
                перетягування стовпця у потрібне положення).
        8. Select Publish to save the view and make it available for other users in your organization. (Змініть порядок стовпців, 
            еретягнувши стовпець у потрібне положення)
    '''
        
        
'Create model-driven app'

'Business rules'

'Security roles'
