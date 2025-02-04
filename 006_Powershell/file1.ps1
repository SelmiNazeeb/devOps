
# if(Test-Path -Path Desktop)
# {
#     write-host "Desktop exists"
# }
# else {
#     write-host "Not exists"
# }
# if (get-Childitem | where-object {$_.name -like "desktop"}) {
 
#if (Test-Path -Path $env:Userprofile\Desktop) {
try {
    $Path=[Environment]::Getfolderpath("broooo")
    echo $Path
    if (Test-Path $Path -pathtype container){
        "desktop folder exsits"
    
    }
    else {
    "folder doesn't exists"
    }
}
catch{
    "error in line number $($_.InvocationInfo.ScriptLineNumber) : $($Error[0])"
} 
