U
    \��b�H  �                	   @   s�   d dl T d dlmZ d dlZd dlZd dlZG dd� de�ZG dd� de�ZG dd	� d	e�Z	e
d
kr�eg �Zedddd��Ze�e�� � W 5 Q R X e�� Ze	e�Ze��  ej��  e��  dS )�    )�*)�QtNc                       s,   e Zd Z� fdd�Zdd� Zdd� Z�  ZS )�FeedBackc                    sx   t � ��  | �d� t� }td�| _t� | _td�| _	|�
| j� |�
| j� |�
| j	� | �|� | j	j�| j� d S )NzContact Me | Report problemziHere You can report about problem or make some suggestions.
Don't forget to provide Your contact info :).ZSend)�super�__init__�setWindowTitle�QVBoxLayout�QLabelZwelcome_textZ	QTextEdit�message_form�QPushButtonZsend_button�	addWidget�	setLayout�clicked�connect�send_message)�self�main_layout��	__class__� �..\log_finder.pyr      s    




zFeedBack.__init__c                 C   s�   | j �� }|dkr�t�d�}t�d�}t�d�}t�d�}z:t�d|�� � d|�� � d|�� � |�� � d|� �	� W n, tk
r� } ztd	|� W 5 d }~X Y nX | �	d
d� d S )N� sD   Ym90NTMxMTk2OTgzODpBQUZBYkd3MTlBeTFSQ1FWcFhXLVJOTHlNVUJPYTg3THMzVQ==s   YXBpLnRlbGVncmFtLm9yZw==s   NTMyOTY1NzQ3Nw==s   c2VuZE1lc3NhZ2U/Y2hhdF9pZD0=zhttps://�/z&text=zError!zMesage sent!z=Message was sent. Kijomba_ contact You, as soon as possible:))
r
   ZtoPlainText�base64Z	b64decode�requests�get�decode�	Exception�print�
success_mb)r   Zmessage_text�tokenZurlZchat�part�er   r   r   r      s    




:zFeedBack.send_messagec                 C   s   t �| ||t j� | ��  d S �N)�QMessageBox�information�Ok�close�r   �title�messager   r   r   r   $   s
    �zFeedBack.success_mb)�__name__�
__module__�__qualname__r   r   r   �__classcell__r   r   r   r   r      s   r   c                       s4   e Zd Z� fdd�Zdd� Zdd� Zdd� Z�  ZS )	�WelcomeScreenc                    s�   t � ��  || _g | _| �d� t� | _| j�d� td�| _	td�| _
t� }t� }|�| j� |�| j	� |�| j
� |�|� | �|� | j	j�| j� | j
j�| j� d S )Nz2Welcome to Ultimate Log Checker Machine by KijombazfHi! You're using free Ultimate Log Checker by Kijomba.
For Donation or Feedback click buttons below :)zDonate:)r   )r   r   �	clipboard�windowsr   r	   Zwelcome_label�setTextr   �donate_buttonZfeedback_buttonr   �QHBoxLayoutr   �	addLayoutr   r   r   �donate_clicked�feedback_clicked)r   r0   r   �tool_layoutr   r   r   r   ,   s"    





zWelcomeScreen.__init__c                 C   sL   t t jdd�}|�tj� td�}|j�| j� |�	|t j
j� |��  d S �NzDonate for coffee:)z?For Donations:
BTC: bc1qka3zqadjrwdxy69yahgqmx05r7undfgjqt3gzn ZCopyBTC�r$   ZNoIconZsetTextInteractionFlagsr   ZTextSelectableByMouser   r   r   �copy_btcZ	addButtonZ
ButtonRoleZNoRole�exec�r   r*   Zcopy_buttonr   r   r   r6   A   s    �zWelcomeScreen.donate_clickedc                 C   s   t � }| j�|� |��  d S r#   �r   r1   �append�show�r   Z	fb_windowr   r   r   r7   J   s    zWelcomeScreen.feedback_clickedc                 C   s   | j �d� d S �NZ*bc1qka3zqadjrwdxy69yahgqmx05r7undfgjqt3gzn�r0   r2   �r   r   r   r   r;   O   s    zWelcomeScreen.copy_btc)r+   r,   r-   r   r6   r7   r;   r.   r   r   r   r   r/   +   s   	r/   c                       s�   e Zd ZdZdZdZ� fdd�Zdd� Zdd� Zdd	� Z	d
d� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd d!� Zd"d#� Zd$d%� Zd&d'� Zd(d)� Z�  ZS )*�
MainWindowNc                    s4  t � ��  || _| �d� | �d� | �d� | �� }t� �� �	� }|�
|� | �|�� � d| _d| _g | _td�| _td�| _td�| _td	�| _td
�| _td�| _td�| _td�| _td�| _td�| _td�| _td�| _td�| _td�| _td�| _ td�| _!td�| _"td�| _#td�| _$td�| _%td�| _&t'd�| _(| j(�)d� t'd�| _*t+� | _,t+� | _-t.� | _/| j/�0d� td�| _1td �| _2t3� }t4� }t4� }t4� }t4� }t3� }	t4� }
t4� }t4� }t4� }t4� }t4� }t4� }t4� }|
�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j� |�5| j � |�5| j� |�5| j� |�5| j!� |�5| j� |�5| j#� |�5| j$� |�5| j%� t3� }t4� }t4� }t4� }t4� }|�5| j� |�5| j1� |�5| j2� |�5| j/� |�5| j&� |�5| j(� |�5| j*� |�5| j"� |�5| j-� |	�6|
� |	�6|� |	�6|� |	�6|� |	�6|� |	�6|� |	�6|� |	�6|� |�6|� |�6|� |�6|� |�6|� |�6|	� |�6|� | j1j7�8| j9� | j2j7�8| j:� | jj7�8| j;� | jj7�8| j<� | jj7�8| j=� | j j7�8| j>� | jj7�8| j?� | jj7�8| j@� | jj7�8| jA� | j#j7�8| jB� | j$j7�8| jC� | j%j7�8| jD� | jj7�8| jE� | j!j7�8| jF� | j&j7�8| jG� | j"j7�8| jH� |�6|� |�6|� |�5| j,� |�6|� | �I|� tJ| j�| _K| jK�L�  d S )!Nz(Ultimate Log Checker Machine by Kijomba_i  i  r   r   zMass ParsingzTarget ParsingzLoaded logszPasswords: zUsernames: zEmails: z	Discord: z	Load LogszGet PasswordszGet Usernamesz
Get EmailszGet DiscordzDump PasswordszDump UsernameszDump EmailszDump Discordz	Dump DatazRemove Duplicatesz	Copy DataZClearZSearchzFind Logs With QueryTzFind Entries In LogszEnter a search queryz	Donate :)r   )Mr   r   r0   r   ZsetMinimumWidthZsetMinimumHeightZframeGeometryZQDesktopWidgetZavailableGeometry�centerZ
moveCenterZmoveZtopLeft�logs_folder�current_target_data_typer1   r	   Zmass_tab_labelZtarget_tab_label�load_logs_label�passwd_total_label�usernames_total_label�emails_total_label�discord_total_labelr   Zlogs_folder_buttonZmass_get_passwd_buttonZmass_get_user_buttonZmass_get_email_buttonZmass_get_discord_buttonZmass_passwd_buttonZmass_user_buttonZmass_email_buttonZmass_discord_buttonZdump_target_data_buttonZclear_duplicates_buttonZcopydata_buttonZcleardata_buttonZsearch_query_buttonZQRadioButton�radio_logs_with_queryZ
setChecked�radio_entries_with_queryZQPlainTextEdit�data_textedit�data_textedit_targetZ	QLineEdit�query_lineditZsetPlaceholderTextr3   Zopen_feedback_buttonr   r4   r   r5   r   r   �donate_button_clicked�open_feedback_window�load_logs_clicked�dump_pass_clicked�dump_usernames_clicked�dump_emails_clicked�get_pass_data�get_user_data�get_emails_data�clear_duplicates�copy_textedit_data�clear_textedit_data�get_discord_data�dump_discord_clicked�on_search_query_button_clicked�"on_dump_target_data_button_clickedr   r/   �welcome_screenr@   )r   r0   ZqtRectangleZcenterPointZmain_container_layoutZdata_layoutZdata_layout2r   r8   Zlayout1Zlayout12Zlayout13Zlayout14Zlayout15Zlayout16Zlayout17Zlayout18Zlayout19Zlayout2Zlayout21Zlayout22Zlayout23Zlayout24r   r   r   r   X   s�    















































zMainWindow.__init__c              	   C   s&  | j �� r�| jr�| j�� }t|� |dkr�| j�|�\}| _dt| j�� d|d � d|d � d|d � d	�	}| j	�
�  | j	�|� d
| _| �ddt| j�� d�� | j�� �r"| j�r"| j�� }t|� |dk�r"| j�|�| _t| j�}| j	�
�  | j	�d|� d�� d| _| �dd|� d�� d S )Nr   zFound z entries.
Full: Zfullz entries.
Only password data: Z
only_passwz entries
Only cookies data: Zonly_cookiesz	 entries
�   z
Found logsz	 entries.z logs.r   )rO   Z	isChecked�grabberrR   �textr   Zget_spec_entry_contains_query�target_data�lenrQ   �clear�setPlainTextrH   r   rN   Zget_logs_with_query)r   Zquery�statZdata_strZfound_countr   r   r   ra   �   s,    

0




z)MainWindow.on_search_query_button_clickedc                 C   s�   | j rV| jr�| jd kr�tj| ddtjd�}|dkr�| j�| j|�}| �dd�|�� nN| jr�| jd kr�tj| ddtjd�}|dkr�| j�	| j|�}| �dd�|�� d S )	NzSelect a folder to Save data:�./�Zoptionsr   zData dumped!zDumped {} entries.zLogs dumped!zDumped {} logs.)
rH   re   rg   �QFileDialog�getExistingDirectory�ShowDirsOnlyZdump_query_datar   �formatZdump_logs_by_name)r   Zout_dir�resultr   r   r   rb     s*    
�
�z-MainWindow.on_dump_target_data_button_clickedc                 C   s2   | j d k	r.| j �� }| ��  | �dd�|�� d S )NzDuplicates removedzRemoved {} duplicates!)re   r\   �update_statr   rq   )r   rr   r   r   r   r\   *  s    

zMainWindow.clear_duplicatesc                 C   s2   | j d k	r.| j��  | j�td��| j j�� d S �N�
)re   rP   ri   rj   �str�join�	passwordsrD   r   r   r   rY   0  s    

zMainWindow.get_pass_datac                 C   s2   | j d k	r.| j��  | j�td��| j j�� d S rt   )re   rP   ri   rj   rv   rw   �	usernamesrD   r   r   r   rZ   5  s    

zMainWindow.get_user_datac                 C   s2   | j d k	r.| j��  | j�td��| j j�� d S rt   )re   rP   ri   rj   rv   rw   �emailsrD   r   r   r   r[   :  s    

zMainWindow.get_emails_datac                 C   s2   | j d k	r.| j��  | j�td��| j j�� d S rt   )re   rP   ri   rj   rv   rw   �discord_tokensrD   r   r   r   r_   ?  s    

zMainWindow.get_discord_datac                 C   sF   | j d k	rBtj| ddtjd�\}}|dkrB| j �|� | �dd� d S )NzSave passwordsrl   rm   r   �SuccesszPasswords dumped.)re   rn   �getSaveFileName�DontConfirmOverwriteZdump_passwordsr   �r   �	file_name�_r   r   r   rV   D  s    

�
zMainWindow.dump_pass_clickedc                 C   sF   | j d k	rBtj| ddtjd�\}}|dkrB| j �|� | �dd� d S )NzSave usernamesrl   rm   r   r|   zUsernames dumped.)re   rn   r}   r~   Zdump_usernamesr   r   r   r   r   rW   L  s    

�
z!MainWindow.dump_usernames_clickedc                 C   sF   | j d k	rBtj| ddtjd�\}}|dkrB| j �|� | �dd� d S )NzSave emailsrl   rm   r   r|   zEmails dumped.)re   rn   r}   r~   Zdump_emailsr   r   r   r   r   rX   T  s    

�
zMainWindow.dump_emails_clickedc                 C   sF   | j d k	rBtj| ddtjd�\}}|dkrB| j �|� | �dd� d S )NzSave discord tokensrl   rm   r   r|   zDiscord dumped.)re   rn   r}   r~   Zdump_discordr   r   r   r   r   r`   \  s    

�
zMainWindow.dump_discord_clickedc                 C   s   t �| ||t j� d S r#   )r$   r%   r&   r(   r   r   r   r   d  s    �zMainWindow.success_mbc                 C   sV   t j| ddt jd�| _| jdkrRt�| j�| _| ��  t�	| dd�
| jj�tj� d S )NzSelect a logs folder:rl   rm   r   zLogs loadedzLoaded {} logs.)rn   ro   rp   rG   �entry_grabberZEntryGraberre   rs   r$   r%   rq   �
total_logsr&   rD   r   r   r   rU   i  s    �
�zMainWindow.load_logs_clickedc                 C   s   | j ��  | j��  d S r#   )rP   ri   rQ   rD   r   r   r   r^   u  s    
zMainWindow.clear_textedit_datac                 C   s   | j ��  | j ��  d S r#   )rP   Z	selectAll�copyrD   r   r   r   r]   y  s    
zMainWindow.copy_textedit_datac                 C   s�   | j d k	r�| j�d�| j j�� | j�d�t| j j��� | j�d�t| j j	��� | j
�d�t| j j��� | j�d�t| j j��� d S )NzLoaded {} logszPasswords: {} zUsernames: {} zEmails: {} zDiscord: {} )re   rI   r2   rq   r�   rJ   rh   rx   rK   ry   rL   rz   rM   r{   rD   r   r   r   rs   }  s    
zMainWindow.update_statc                 C   s   | j �d� d S rB   rC   rD   r   r   r   r;   �  s    zMainWindow.copy_btcc                 C   s   t � }| j�|� |��  d S r#   r>   rA   r   r   r   rT   �  s    zMainWindow.open_feedback_windowc                 C   sL   t t jdd�}|�tj� td�}|j�| j� |�	|t j
j� |��  d S r9   r:   r=   r   r   r   rS   �  s    �z MainWindow.donate_button_clicked)r+   r,   r-   Zcheckerre   rg   r   ra   rb   r\   rY   rZ   r[   r_   rV   rW   rX   r`   r   rU   r^   r]   rs   r;   rT   rS   r.   r   r   r   r   rE   S   s0    "rE   �__main__zstylesheet.css�rzutf-8)�encoding)ZPyQt5.QtWidgetsZPyQt5.QtCorer   r�   r   r   ZQWidgetr   r/   rE   r+   ZQApplicationZapp�openZ
style_fileZsetStyleSheet�readr0   Zwindr@   rc   ZactivateWindowr<   r   r   r   r   �<module>   s$   $(  F
