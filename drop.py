import dropbox

dropbox_access_token= "sl.BJiLNz8xkGrTKK74AXk1JYxs9Z3YfKmh96nKA68-4wyhq8A9YPWczZ2moWLrvk_rf7PGAyOmH9NlbUu8NIemmM7W5VT9_LhWOBkhLtYFPc_M9_dNz4GU9lXTe4amoqCwdzLa2QQ"    #Enter your own access token
dropbox_path= "/19IT112/me.png"
computer_path="C:/Users/Tarun Kishore/Pictures/mypic.png"

client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")

client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))

metadata,f = client.files_download("/19IT112/me.png")
out = open("hello_download.png",'wb')
out.write(f.content)
out.close()
print("[SUCCESS] DOWNLOADED")