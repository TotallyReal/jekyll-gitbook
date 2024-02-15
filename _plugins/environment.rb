require 'base64'

module Jekyll
  class Environment < Generator
    priority :low

    def generate(site)
      puts "------------------+++++++++++++++++++++++++++----------------"
      
      site.collections["pages"].docs.each do |doc|
        # puts File.basename(doc.path, '.*')
        if File.basename(doc.path, '.*') != 'hebrew_motivation'
          mod_content = `python _scripts\\converter.py '#{Base64.strict_encode64(doc.content)}'`
          doc.content = mod_content
        end
      end

      # c = site.collections["pages"]

      # input = c.docs[0].content
      
      # modified_s = `python scripts\\converter.py '#{Base64.strict_encode64(input)}'`
      # c.docs[0].content = modified_s
      # puts modified_s

      puts "--------------------------------------------------------------------"
    end
  end
end

def print_variables(obj)
  puts "# #{obj.class}"
  obj.instance_variables.each do |var|
    var_name = var.to_s.delete('@')
    var_value = obj.instance_variable_get(var)
    var_type = var_value.class
    puts "#{var_name}: #{var_type}"
  end
end

def print_pages()  
  site.pages.each do |page|
    # Print the path and name of the page
    puts "Path: #{page.path}, Name: #{page.name}"
  end
end



